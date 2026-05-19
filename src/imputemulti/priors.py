"""Implementation of data-dependent priors and level counting utilities."""

import pandas as pd
import numpy as np
from typing import Optional, Union, Literal
from .utils import expand_grid, fact_to_int, get_levels
from ._internal_rust import count_compare_rust

def count_levels(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """Count occurrences of patterns in dat matching enum_list."""
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def data_dep_prior_multi(dat: pd.DataFrame) -> pd.DataFrame:
    """Create a data dependent prior for p-dimensional multinomial distributions."""
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def check_prior(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None, verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """Check and process the conjugate prior."""
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res
