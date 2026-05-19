import pandas as pd
from importlib import resources

def load_tract2221() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("imputemulti.data").joinpath("tract2221.parquet")
    return pd.read_parquet(path)
