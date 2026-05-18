import pytest
import pandas as pd
import numpy as np
from imputemulti.priors import count_levels, data_dep_prior_multi, check_prior
from imputemulti import load_tract2221

# --- Feature: F-201 — Python Data Models and Priors ---
# Spec version: 1.1.0
# Layer: python
# Satisfies: data_dep_prior_multi produces alpha values consistent with R implementation for tract2221.

def test_count_levels_no_na():
    """
    Test count_levels with complete data.
    """
    df = pd.DataFrame({
        'A': pd.Series(['a', 'a', 'b'], dtype='category'),
        'B': pd.Series(['x', 'x', 'y'], dtype='category')
    })
    enum = pd.DataFrame({
        'A': pd.Series(['a', 'a', 'b', 'b'], dtype='category'),
        'B': pd.Series(['x', 'y', 'x', 'y'], dtype='category')
    })
    
    res = count_levels(df, enum, has_na="no")
    # Should only return rows with counts > 0
    # ('a', 'x') count 2
    # ('b', 'y') count 1
    assert len(res) == 2
    assert res.loc[(res['A'] == 'a') & (res['B'] == 'x'), 'counts'].iloc[0] == 2
    assert res.loc[(res['A'] == 'b') & (res['B'] == 'y'), 'counts'].iloc[0] == 1

def test_data_dep_prior_structure():
    """
    Verify structure of data_dep_prior_multi output.
    """
    df = load_tract2221().iloc[:50]
    prior = data_dep_prior_multi(df)
    
    assert isinstance(prior, pd.DataFrame)
    assert 'alpha' in prior.columns
    assert len(prior) > 0
    # All alpha should be >= 1 (due to fillna(1))
    assert (prior['alpha'] >= 1).all()

def test_check_prior_flat():
    """
    Test check_prior with flat prior.
    """
    dat = pd.DataFrame({'A': [1], 'B': [2]})
    res = check_prior(dat, conj_prior="flat.prior", alpha=2.0, outer=True)
    assert res == 2.0
    
    with pytest.raises(ValueError, match="Flat priors must be supplied as a scalar."):
        check_prior(dat, conj_prior="flat.prior", alpha="bad", outer=True)

def test_check_prior_non_informative():
    """
    Test check_prior with non-informative prior.
    """
    dat = pd.DataFrame({'A': [1], 'B': [2]})
    res = check_prior(dat, conj_prior="non.informative", outer=True)
    assert res == 1.0
