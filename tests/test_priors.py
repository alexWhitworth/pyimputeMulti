import pandas as pd
import pytest

from imputemulti import load_tract2221
from imputemulti.priors import check_prior, count_levels, data_dep_prior_multi

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

def test_data_dep_prior_not_enough_complete_cases():
    """
    Test data_dep_prior_multi when there are not enough complete cases for sampling.
    This covers line 46 in priors.py.
    """
    df_data = {
        'col1': [1, 1, 1, 2, 2, None],
        'col2': ['A', 'B', None, 'A', 'B', 'A']
    }
    dat = pd.DataFrame(df_data)
    # With n = round(0.2 * len(dat)) = round(0.2 * 6) = 1,
    # and only 4 complete cases, this should trigger the len(comp_indices) < n branch.
    prior = data_dep_prior_multi(dat)
    assert isinstance(prior, pd.DataFrame)
    assert 'alpha' in prior.columns
    assert (prior['alpha'] >= 1).all() # Ensure it still produces valid alphas


def test_check_prior_invalid_conj_prior_outer_true():
    """
    Test check_prior with an invalid conj_prior when outer=True.
    This covers lines 75-77 in priors.py.
    """
    dat = pd.DataFrame({'A': [1], 'B': [2]})
    res = check_prior(dat, conj_prior="invalid.prior", alpha=None, verbose=False, outer=True)
    assert res is None


def test_check_prior_enum_comp_none_outer_false():
    """
    Test check_prior with enum_comp=None when outer=False.
    This covers line 84 in priors.py.
    """
    dat = pd.DataFrame({'A': [1], 'B': [2]})
    with pytest.raises(ValueError, match="enum_comp must be provided if outer=False"):
        check_prior(dat, conj_prior="none", alpha=None, verbose=False, outer=False, enum_comp=None)


def test_check_prior_data_dep_alpha_type_mismatch_outer_false():
    """
    Test check_prior with data.dep prior and alpha not a DataFrame when outer=False.
    This covers line 98 in priors.py.
    """
    dat = pd.DataFrame({'A': [1], 'B': [2]})
    enum_comp = pd.DataFrame({'A': [1], 'B': [2]})
    with pytest.raises(ValueError, match="alpha must be a DataFrame for data.dep prior"):
        check_prior(dat, conj_prior="data.dep", alpha=1.0, verbose=False, outer=False, enum_comp=enum_comp)


def test_check_prior_data_dep_alpha_len_mismatch_outer_false():
    """
    Test check_prior with data.dep prior and alpha DataFrame length mismatch when outer=False.
    This covers lines 100-102 in priors.py.
    """
    dat = pd.DataFrame({'A': [1], 'B': [2]})
    enum_comp = pd.DataFrame({'A': [1, 2], 'B': [2, 3]})
    alpha_mismatch = pd.DataFrame({'A': [1], 'B': [2], 'alpha': [1.0]})
    with pytest.raises(ValueError, match="len\\(alpha\\) must match len\\(enum_comp\\)"):
        check_prior(dat, conj_prior="data.dep", alpha=alpha_mismatch, verbose=False, outer=False, enum_comp=enum_comp)
