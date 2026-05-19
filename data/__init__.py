import pathlib

import pandas as pd


def load_tract2221() -> pd.DataFrame:
    """
    Load the tract2221 dataset.

    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = pathlib.Path(__file__).parent / "tract2221.parquet"
    return pd.read_parquet(path)
