import pytest
import pandas as pd
import numpy as np
from imputemulti.algorithms import multinomial_em, multinomial_data_aug, multinomial_impute, multinomial_stats
from imputemulti.utils import expand_grid

# --- Feature: F-202 — EM and DA Algorithms ---
# Spec version: 1.1.0
# Layer: python
# Satisfies: multinomial_em converges to MLE matching reference.
# Satisfies: multinomial_impute correctly fills NAs.

def test_multinomial_em_synthetic():
    """
    Test EM on a simple synthetic case where MLE is known.
    A=0, B=0: 40
    A=1, B=1: 40
    A=0, B=NA: 20
    Expected MLE: theta(0,0)=0.6, theta(1,1)=0.4, others=0
    """
    df = pd.DataFrame({
        'A': pd.Series([0]*40 + [1]*40 + [0]*20, dtype='category'),
        'B': pd.Series([0]*40 + [1]*40 + [np.nan]*20, dtype='category')
    })
    
    enum_comp = expand_grid({'A': [0, 1], 'B': [0, 1]})
    n_obs = len(df)
    
    x_y = multinomial_stats(df, output="x_y")
    z_Os_y = multinomial_stats(df, output="z_Os_y")
    
    res = multinomial_em(x_y, z_Os_y, enum_comp, n_obs, conj_prior="none", tol=1e-10)
    
    mle = res.mle_x_y
    # Find (0,0)
    theta_00 = mle.loc[(mle['A'] == 0) & (mle['B'] == 0), 'theta_y'].iloc[0]
    theta_11 = mle.loc[(mle['A'] == 1) & (mle['B'] == 1), 'theta_y'].iloc[0]
    
    np.testing.assert_allclose(theta_00, 0.6, atol=1e-6)
    np.testing.assert_allclose(theta_11, 0.4, atol=1e-6)
    assert mle['theta_y'].sum() == pytest.approx(1.0)

def test_multinomial_impute_fills_nas():
    """
    Verify that multinomial_impute fills all NAs.
    """
    df = pd.DataFrame({
        'A': pd.Series([0, 1, 0, np.nan], dtype='category'),
        'B': pd.Series([0, 1, np.nan, 1], dtype='category')
    })
    
    res = multinomial_impute(df, method="EM", conj_prior="none")
    imputed = res.data[1]
    
    assert imputed.isna().sum().sum() == 0
    assert len(imputed) == 4

def test_multinomial_da_synthetic():
    """
    Test DA on the same synthetic case. 
    Results should be close to EM MLE with enough draws.
    """
    np.random.seed(42)  # Set seed for stability
    df = pd.DataFrame({
        'A': pd.Series([0]*40 + [1]*40 + [0]*20, dtype='category'),
        'B': pd.Series([0]*40 + [1]*40 + [np.nan]*20, dtype='category')
    })
    
    enum_comp = expand_grid({'A': [0, 1], 'B': [0, 1]})
    n_obs = len(df)
    
    x_y = multinomial_stats(df, output="x_y")
    z_Os_y = multinomial_stats(df, output="z_Os_y")
    
    # Use many draws for stability
    res = multinomial_data_aug(x_y, z_Os_y, enum_comp, n_obs, 
                               conj_prior="none", burnin=100, post_draws=1000)
    
    mle = res.mle_x_y
    theta_00 = mle.loc[(mle['A'] == 0) & (mle['B'] == 0), 'theta_y'].iloc[0]
    theta_11 = mle.loc[(mle['A'] == 1) & (mle['B'] == 1), 'theta_y'].iloc[0]
    
    # DA is stochastic, so use wider tolerance
    np.testing.assert_allclose(theta_00, 0.6, atol=0.05)
    np.testing.assert_allclose(theta_11, 0.4, atol=0.05)

def test_multinomial_em_edge_empty():
    """
    Test EM with empty dataframe.
    """
    df = pd.DataFrame({'A': pd.Series([], dtype='category'), 'B': pd.Series([], dtype='category')})
    enum_comp = expand_grid({'A': [0, 1], 'B': [0, 1]})
    
    # Should handle empty input gracefully
    # This might require some defensive coding in multinomial_stats
    x_y = multinomial_stats(df, output="x_y")
    z_Os_y = multinomial_stats(df, output="z_Os_y")
    
    res = multinomial_em(x_y, z_Os_y, enum_comp, n_obs=0, conj_prior="non.informative")
    assert res.mle_iter >= 0

def test_multinomial_impute_all_na():
    """
    Test imputation where all values are NA.
    """
    df = pd.DataFrame({
        'A': pd.Series([np.nan, np.nan], dtype='category'),
        'B': pd.Series([np.nan, np.nan], dtype='category')
    })
    # Set levels explicitly since they can't be inferred from all-NA
    df['A'] = df['A'].cat.add_categories([0, 1])
    df['B'] = df['B'].cat.add_categories([0, 1])
    
    res = multinomial_impute(df, method="EM", conj_prior="non.informative")
    imputed = res.data[1]
    assert imputed.isna().sum().sum() == 0
    assert len(imputed) == 2
