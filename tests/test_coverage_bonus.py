import numpy as np
import pandas as pd
import pytest

from imputemulti.algorithms import (
    multinomial_em,
    multinomial_impute,
    multinomial_stats,
)
from imputemulti.priors import check_prior
from imputemulti.utils import expand_grid

# --- Feature: F-401 — Testing, Benchmarking and Validation ---
# Phase 4
# Layer: ffi_boundary


def test_priors_additional_coverage():
    """
    Test additional branches in priors.py for coverage.
    """
    df = pd.DataFrame({
        'A': pd.Series([0, 1, 0, 1], dtype='category'),
        'B': pd.Series([0, 0, 1, 1], dtype='category')
    })
    enum = expand_grid({'A': [0, 1], 'B': [0, 1]})

    # data.dep with user-supplied alpha
    alpha = pd.DataFrame({
        'A': [0, 1, 0, 1],
        'B': [0, 0, 1, 1],
        'alpha': [1.0, 2.0, 3.0, 4.0]
    })
    res = check_prior(df, conj_prior="data.dep", alpha=alpha, outer=True, verbose=True)
    pd.testing.assert_frame_equal(res, alpha)

    # outer=False error path
    with pytest.raises(ValueError, match="enum_comp must be provided if outer=False"):
        check_prior(df, outer=False, enum_comp=None)

    # data.dep inner error paths
    with pytest.raises(ValueError, match="alpha must be a DataFrame for data.dep prior"):
        check_prior(df, conj_prior="data.dep", alpha=1.0, outer=False, enum_comp=enum)

    alpha_bad_len = alpha.iloc[:2]
    with pytest.raises(ValueError, match=r"len\(alpha\) must match len\(enum_comp\)"):
        check_prior(df, conj_prior="data.dep", alpha=alpha_bad_len, outer=False, enum_comp=enum)


def test_algorithms_additional_coverage():
    """
    Test additional branches in algorithms.py for coverage.
    """
    df = pd.DataFrame({
        'A': pd.Series([0, 1], dtype='category'),
        'B': pd.Series([0, 1], dtype='category')
    })

    # multinomial_stats possible.obs
    res = multinomial_stats(df, output="possible.obs")
    assert len(res) == 4

    # multinomial_em with verbose
    x_y = multinomial_stats(df, output="x_y")
    z_os_y = multinomial_stats(df, output="z_os_y")
    enum = multinomial_stats(df, output="possible.obs")
    multinomial_em(x_y, z_os_y, enum, n_obs=2, verbose=True, max_iter=1)


def test_multinomial_impute_verbose():
    """
    Test multinomial_impute with verbose=True.
    """
    df = pd.DataFrame({
        'A': pd.Series([0, np.nan], dtype='category'),
        'B': pd.Series([0, 1], dtype='category')
    })
    multinomial_impute(df, verbose=True)


def test_get_levels_non_categorical():
    """
    Test get_levels with non-categorical data.
    """
    from imputemulti.utils import get_levels
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    levels = get_levels(df)
    assert 1 in levels['A']
    assert 3 in levels['B']
