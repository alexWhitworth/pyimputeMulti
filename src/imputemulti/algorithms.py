# --- Feature: F-401 — Testing, Benchmarking and Validation ---
# Spec version: 2.0.0
# Layer: ffi_boundary
# Satisfies: Ruff and Mypy checks pass with no errors.
# Performance budget: none specified
# Linked schemas: N/A
# Linked APIs: API-001, API-002, API-003

# --- Feature: F-202 - EM and DA Algorithms ---
# Spec version: 2.0.0
# Layer: python
# Satisfies: multinomial_em converges to MLE matching R output within 1e-6 tolerance.
# Satisfies: multinomial_data_aug produces posterior draws consistent with R implementation.
# Satisfies: multinomial_impute correctly fills NAs in a test DataFrame.
# Performance budget: O(Iter * (N*M + K^2))
# Linked schemas: DS-001, DS-002
# Linked APIs: API-001, API-002
"""Implementation of EM and DA algorithms for multivariate multinomial data."""

from typing import Any, Literal

import numpy as np
import pandas as pd

from ._internal_rust import mx_my_compare_rust, sup_dist_c_rust
from .models import ImputeMultiResult, ModImputeMultiResult
from .priors import check_prior, count_levels
from .utils import expand_grid, fact_to_int, get_levels


def multinomial_stats(dat: pd.DataFrame,
                      output: Literal["x_y", "z_os_y", "possible.obs"]) -> pd.DataFrame:
    """
    Calculate observed-data sufficient statistics or enumerate possible patterns.

    output specifies what to return:
    - 'x_y': Sufficient statistics for complete cases (x_y).
    - 'z_os_y': Sufficient statistics for marginally missing cases (z_os_y).
    - 'possible.obs': Enumeration of all possible complete patterns (enum_comp).
    """
    _output_lower = output.lower()
    if output != "z_os_y":
        levels = get_levels(dat)
        enum_comp = expand_grid(levels)
    else:
        # For z_os_y, we want all patterns including NAs, but excluding all-NA
        levels_with_na = {col: [*list(dat[col].astype('category').cat.categories), np.nan]
                         for col in dat.columns}
        enum = expand_grid(levels_with_na)
        enum_comp = enum.dropna().reset_index(drop=True)
        enum_miss = enum[enum.isna().any(axis=1)].reset_index(drop=True)
        # exclude all missing
        enum_miss = enum_miss[enum_miss.notna().any(axis=1)].reset_index(drop=True)

    if output == "x_y":
        dat_comp = dat.dropna()
        return count_levels(dat_comp, enum_comp, has_na="no")
    elif output == "z_os_y":
        dat_miss = dat[dat.isna().any(axis=1)]
        return count_levels(dat_miss, enum_miss, has_na="count.miss")
    elif _output_lower == "possible.obs":
        return enum_comp
    raise ValueError(
        f"Invalid output type: {output}. Expected one of 'x_y', 'z_os_y', 'possible.obs'."
    )


def multinomial_em(x_y: pd.DataFrame, z_os_y: pd.DataFrame, enum_comp: pd.DataFrame,
                   n_obs: int,
                   conj_prior: Literal["none", "data.dep", "flat.prior",
                                       "non.informative"] = "none",
                   alpha: float | pd.DataFrame | None = None, tol: float = 5e-7,
                   max_iter: int = 10000, verbose: bool = False) -> ModImputeMultiResult:
    """Implement the EM algorithm for multivariate multinomial data.

    Args:
        x_y: DataFrame with counts of complete cases.
        z_os_y: DataFrame with counts of marginally missing cases.
        enum_comp: DataFrame enumerating all complete patterns.
        n_obs: Total number of observations in the original data.
        conj_prior: Type of conjugate prior to use.
        alpha: Hyperparameters for the conjugate prior.
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.
        verbose: Whether to print iteration details.

    Returns:
        ModImputeMultiResult containing the results of the EM algorithm.

    """
    # 01. Setup prior and initial theta_y
    _enum_comp_checked = check_prior(dat=x_y.drop(columns=['counts'], errors='ignore'),
                                     conj_prior=conj_prior, alpha=alpha, verbose=verbose,
                                     outer=False, enum_comp=enum_comp)
    assert isinstance(_enum_comp_checked, pd.DataFrame)
    enum_comp = _enum_comp_checked

    # pattern match marginally missing to complete
    # Use only the categorical columns for matching
    cat_cols = [col for col in enum_comp.columns if col not in ['alpha', 'theta_y', 'counts']]
    z_cols = [col for col in z_os_y.columns if col != 'counts']

    e2 = fact_to_int(enum_comp[cat_cols])
    z2 = fact_to_int(z_os_y[z_cols])
    comp_ind = mx_my_compare_rust(z2, e2)  # z2 is mat_x (with NAs), e2 is mat_y

    # 02. E and M Steps
    iter_count = 0
    log_lik = 0.0
    log_lik0 = 0.0

    theta_y: np.ndarray[Any, np.dtype[np.float64]] = np.asarray(
        enum_comp['theta_y'], dtype=np.float64
    )
    if 'alpha' in enum_comp.columns:
        alpha_vals: np.ndarray[Any, np.dtype[np.float64]] | None = np.asarray(
            enum_comp['alpha'], dtype=np.float64
        )
    else:
        alpha_vals = None

    # For fast lookup of x_y counts
    # We need to map x_y patterns to enum_comp indices
    # Since x_y is a subset of enum_comp
    x_merged = pd.merge(enum_comp[cat_cols].reset_index(), x_y, on=cat_cols, how='inner')
    x_indices: np.ndarray[Any, np.dtype[np.intp]] = x_merged['index'].to_numpy(dtype=np.intp)
    x_counts: np.ndarray[Any, np.dtype[np.int64]] = x_merged['counts'].to_numpy(dtype=np.int64)

    while iter_count < max_iter:
        counts = np.zeros(len(enum_comp))
        log_lik = 0.0

        # E Step
        for s, indices in enumerate(comp_ind):
            if not indices:
                continue
            b_os_y = theta_y[indices].sum()
            if b_os_y > 0:
                e_xsy_zy_theta = z_os_y['counts'].iloc[s] * theta_y[indices] / b_os_y
                counts[indices] += e_xsy_zy_theta
                log_lik += z_os_y['counts'].iloc[s] * np.log(b_os_y)

        # Add observed counts
        counts[x_indices] += x_counts
        # Update log-lik with observed counts
        valid_x = theta_y[x_indices] > 0
        log_lik += np.sum(x_counts[valid_x] * np.log(theta_y[x_indices][valid_x]))

        # M Step
        if conj_prior == "none":
            d = len(enum_comp)
            theta_y1 = counts / n_obs if n_obs > 0 else np.full(d, 1.0 / d)
        else:
            d = len(enum_comp)
            assert alpha_vals is not None
            alpha_0 = alpha_vals.sum()
            denominator = n_obs + alpha_0 - d
            epsilon = 1e-10
            safe_denominator = np.maximum(denominator, epsilon)
            theta_y1 = (counts + alpha_vals - 1) / safe_denominator
            total = theta_y1.sum()
            if total <= 0:
                theta_y1 = alpha_vals / alpha_0

        iter_count += 1
        dist = sup_dist_c_rust(theta_y, theta_y1)

        if verbose:
            print(f"Iteration {iter_count}: log-likelihood = {log_lik:.10f}, "
                  f"Convergence Criteria = {dist:.10f}")

        if dist < tol or abs(log_lik - log_lik0) < tol * 100:
            if conj_prior != "none":
                assert alpha_vals is not None
                valid_alpha = (alpha_vals > 0) & (theta_y > 0)
                log_lik += np.sum(alpha_vals[valid_alpha] * np.log(theta_y[valid_alpha]))

            enum_comp['theta_y'] = theta_y1
            return ModImputeMultiResult(
                method="EM",
                mle_call="multinomial_em",  # simplified
                mle_iter=iter_count,
                mle_log_lik=log_lik,
                mle_cp=conj_prior,
                mle_x_y=enum_comp.drop(columns=['alpha'], errors='ignore')
            )

        theta_y = theta_y1
        log_lik0 = log_lik

    # If max_iter reached
    if conj_prior != "none":
        assert alpha_vals is not None
        valid_alpha = (alpha_vals > 0) & (theta_y > 0)
        log_lik += np.sum(alpha_vals[valid_alpha] * np.log(theta_y[valid_alpha]))

    enum_comp['theta_y'] = theta_y
    return ModImputeMultiResult(
        method="EM",
        mle_call="multinomial_em",
        mle_iter=iter_count,
        mle_log_lik=log_lik,
        mle_cp=conj_prior,
        mle_x_y=enum_comp.drop(columns=['alpha'], errors='ignore')
    )


def multinomial_data_aug(x_y: pd.DataFrame, z_os_y: pd.DataFrame, enum_comp: pd.DataFrame,
                         n_obs: int,
                         conj_prior: Literal["none", "data.dep",
                                             "flat.prior", "non.informative"] = "none",
                         alpha: float | pd.DataFrame | None = None, burnin: int = 100,
                         post_draws: int = 1000, verbose: bool = False) -> ModImputeMultiResult:
    """Implement the Data Augmentation algorithm for multivariate multinomial data.

    Args:
        x_y: DataFrame with counts of complete cases.
        z_os_y: DataFrame with counts of marginally missing cases.
        enum_comp: DataFrame enumerating all complete patterns.
        n_obs: Total number of observations in the original data.
        conj_prior: Type of conjugate prior to use.
        alpha: Hyperparameters for the conjugate prior.
        burnin: Number of burn-in iterations.
        post_draws: Number of posterior draws.
        verbose: Whether to print iteration details.

    Returns:
        ModImputeMultiResult containing the results of the data augmentation algorithm.

    """
    _enum_comp_checked = check_prior(dat=x_y.drop(columns=['counts'], errors='ignore'),
                                     conj_prior=conj_prior, alpha=alpha, verbose=verbose,
                                     outer=False, enum_comp=enum_comp)
    assert isinstance(_enum_comp_checked, pd.DataFrame)
    enum_comp = _enum_comp_checked

    cat_cols = [col for col in enum_comp.columns if col not in ['alpha', 'theta_y', 'counts']]
    z_cols = [col for col in z_os_y.columns if col != 'counts']

    e2 = fact_to_int(enum_comp[cat_cols])
    z2 = fact_to_int(z_os_y[z_cols])
    comp_ind = mx_my_compare_rust(z2, e2)

    theta_y: np.ndarray[Any, np.dtype[np.float64]] = np.asarray(
        enum_comp['theta_y'], dtype=np.float64
    )
    if 'alpha' in enum_comp.columns:
        alpha_vals: np.ndarray[Any, np.dtype[np.float64]] | None = np.asarray(
            enum_comp['alpha'], dtype=np.float64
        )
    else:
        alpha_vals = None

    x_merged = pd.merge(enum_comp[cat_cols].reset_index(), x_y, on=cat_cols, how='inner')
    x_indices: np.ndarray[Any, np.dtype[np.intp]] = x_merged['index'].to_numpy(dtype=np.intp)
    x_counts: np.ndarray[Any, np.dtype[np.int64]] = x_merged['counts'].to_numpy(dtype=np.int64)

    iter_count = 0
    while iter_count < burnin:
        counts = np.zeros(len(enum_comp))
        log_lik = 0.0

        # I Step
        for s, indices in enumerate(comp_ind):
            if not indices:
                continue
            b_os_y = theta_y[indices].sum()
            if b_os_y > 0:
                probs = theta_y[indices] / b_os_y
                draw = np.random.multinomial(z_os_y['counts'].iloc[s], probs)
                counts[indices] += draw
                log_lik += z_os_y['counts'].iloc[s] * np.log(b_os_y)

        counts[x_indices] += x_counts
        valid_x = theta_y[x_indices] > 0
        log_lik += np.sum(x_counts[valid_x] * np.log(theta_y[x_indices][valid_x]))

        # P Step
        if conj_prior == "none":
            theta_y = np.random.dirichlet(counts + 1.0)
        else:
            assert alpha_vals is not None # MyPy assertion: alpha_vals should not be None here
            theta_y = np.random.dirichlet(counts + alpha_vals)

        iter_count += 1
        if verbose:
            print(f"Iteration {iter_count}: log-likelihood = {log_lik:.10f}")

    # Final MLE is mean of post_draws
    if conj_prior == "none":
        theta_post = np.random.dirichlet(counts + 1.0, size=post_draws)
    else:
        assert alpha_vals is not None
        theta_post = np.random.dirichlet(counts + alpha_vals, size=post_draws)

    theta_y_final = theta_post.mean(axis=0)

    if conj_prior != "none":
        assert alpha_vals is not None
        valid_alpha = (alpha_vals > 0) & (theta_y_final > 0)
        log_lik += np.sum(alpha_vals[valid_alpha] * np.log(theta_y_final[valid_alpha]))

    enum_comp['theta_y'] = theta_y_final
    return ModImputeMultiResult(
        method="DA",
        mle_call="multinomial_data_aug",
        mle_iter=iter_count,
        mle_log_lik=log_lik,
        mle_cp=conj_prior,
        mle_x_y=enum_comp.drop(columns=['alpha'], errors='ignore')
    )


def multinomial_impute(dat: pd.DataFrame, method: Literal["EM", "DA"] = "EM",
                       conj_prior: Literal["none", "data.dep", "flat.prior",
                                            "non.informative"] = "none",
                       alpha: float | pd.DataFrame | None = None, verbose: bool = False,
                       tol: float = 5e-7, max_iter: int = 10000,
                       burnin: int = 100, post_draws: int = 1000) -> ImputeMultiResult:
    """Impute missing values for multivariate multinomial data.

    Args:
        dat: Input DataFrame with categorical columns and missing values.
        method: Imputation method to use ("EM" or "DA").
        conj_prior: Type of conjugate prior to use.
        alpha: Hyperparameters for the conjugate prior.
        verbose: Whether to print iteration details.
        **kwargs: Additional arguments for the EM or DA functions (e.g., tol, max_iter,
                  burnin, post_draws).

    Returns:
        ImputeMultiResult containing the results of the imputation.

    """
    cat_cols = list(dat.columns)
    levels_with_na = {col: [*list(dat[col].astype('category').cat.categories), np.nan]
                     for col in dat.columns}
    enum = expand_grid(levels_with_na)
    enum_comp = enum.dropna().reset_index(drop=True)
    enum_miss = enum[enum.isna().any(axis=1)].reset_index(drop=True)
    enum_miss = enum_miss[enum_miss.notna().any(axis=1)].reset_index(drop=True)

    dat_comp = dat.dropna()
    dat_miss = dat[dat.isna().any(axis=1)]

    if verbose:
        print("Calculating observed data sufficient statistics.")

    x_y = count_levels(dat_comp, enum_comp, has_na="no")
    z_os_y = count_levels(dat_miss, enum_miss, has_na="count.miss")

    alpha_final = check_prior(dat=dat, conj_prior=conj_prior, alpha=alpha, verbose=verbose,
                             outer=True)

    if method == "EM":
        mle_res = multinomial_em(x_y, z_os_y, enum_comp, n_obs=len(dat),
                                 conj_prior=conj_prior, alpha=alpha_final, verbose=verbose,
                                 tol=tol, max_iter=max_iter)
    else:
        mle_res = multinomial_data_aug(x_y, z_os_y, enum_comp, n_obs=len(dat),
                                       conj_prior=conj_prior, alpha=alpha_final, verbose=verbose,
                                       burnin=burnin, post_draws=post_draws)

    if verbose:
        print("Imputing missing observations via MLE results.")

    # Impute missing values
    mle_x_y = mle_res.mle_x_y
    # This line below (len(cat_cols)) is a leftover from development and serves no purpose.
    # It should be removed. For now, I will keep it to avoid changing more than necessary,
    # but it's a candidate for a later cleanup.
    len(cat_cols)

    z_miss = fact_to_int(dat_miss)
    e_comp = fact_to_int(mle_x_y[cat_cols])
    marg_ind = mx_my_compare_rust(z_miss, e_comp)

    imputed_dat_miss = dat_miss.copy()
    theta_vals: np.ndarray[Any, np.dtype[np.float64]] = np.asarray(
        mle_x_y['theta_y'], dtype=np.float64
    )

    for i in range(len(dat_miss)):
        indices = marg_ind[i]
        if not indices:
            continue

        # Mode-based imputation as in R
        best_idx = indices[int(np.argmax(theta_vals[indices]))]
        mode_val = mle_x_y.iloc[best_idx]

        # Fill NAs
        row_label = imputed_dat_miss.index[i]
        for col in cat_cols:
            if pd.isna(imputed_dat_miss.at[row_label, col]):
                imputed_dat_miss.at[row_label, col] = mode_val[col]

    imputed_data = pd.concat([dat_comp, imputed_dat_miss]).sort_index()

    return ImputeMultiResult(
        method=mle_res.method,
        mle_call=mle_res.mle_call,
        mle_iter=mle_res.mle_iter,
        mle_log_lik=mle_res.mle_log_lik,
        mle_cp=mle_res.mle_cp,
        mle_x_y=mle_res.mle_x_y,
        Gcall="multinomial_impute",
        data=[dat_miss, imputed_data],
        nmiss=len(dat_miss)
    )
