import pandas as pd

from imputemulti import load_tract2221, multinomial_impute


def test_full_imputation_em():
    df = load_tract2221()
    # Use a small subset for faster testing
    df_sub = df.iloc[:100, :4]

    res = multinomial_impute(df_sub, method="EM", conj_prior="none", max_iter=10)

    assert res.method == "EM"
    assert isinstance(res.data[1], pd.DataFrame)
    assert res.data[1].isna().sum().sum() == 0
    assert len(res.data[1]) == len(df_sub)

def test_full_imputation_da():
    df = load_tract2221()
    df_sub = df.iloc[:100, :4]

    res = multinomial_impute(df_sub, method="DA", conj_prior="non.informative",
                             burnin=5, post_draws=10)

    assert res.method == "DA"
    assert isinstance(res.data[1], pd.DataFrame)
    assert res.data[1].isna().sum().sum() == 0
    assert len(res.data[1]) == len(df_sub)
