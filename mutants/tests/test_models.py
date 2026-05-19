import pytest
import pandas as pd
import numpy as np
from imputemulti.models import ImputeMultiResult, ModImputeMultiResult

# --- Feature: F-201 — Python Data Models and Priors ---
# Spec version: 1.1.0
# Layer: python
# Satisfies: ImputeMultiResult is immutable and validates field types.

def test_impute_multi_result_immutability():
    """
    Test that ImputeMultiResult is immutable (@dataclass(frozen=True)).
    """
    df = pd.DataFrame({'A': [1], 'B': [2]})
    res = ImputeMultiResult(
        method="EM",
        mle_call="multinomial_impute",
        mle_iter=10,
        mle_log_lik=-100.0,
        mle_cp="none",
        mle_x_y=df,
        Gcall="multinomial_impute",
        data=[df, df],
        nmiss=0
    )
    
    with pytest.raises(AttributeError):
        res.method = "DA"

def test_mod_impute_multi_result_immutability():
    """
    Test that ModImputeMultiResult is immutable.
    """
    df = pd.DataFrame({'A': [1], 'B': [2]})
    res = ModImputeMultiResult(
        method="EM",
        mle_call="multinomial_em",
        mle_iter=10,
        mle_log_lik=-100.0,
        mle_cp="none",
        mle_x_y=df
    )
    
    with pytest.raises(AttributeError):
        res.method = "DA"

def test_mod_impute_multi_result_fields():
    """
    Verify fields of ModImputeMultiResult.
    """
    df = pd.DataFrame({'theta_y': [0.5, 0.5]})
    res = ModImputeMultiResult(
        method="EM",
        mle_call="multinomial_em",
        mle_iter=10,
        mle_log_lik=-100.0,
        mle_cp="none",
        mle_x_y=df
    )
    assert res.method == "EM"
    assert res.mle_iter == 10
    assert res.mle_log_lik == -100.0
    pd.testing.assert_frame_equal(res.mle_x_y, df)
