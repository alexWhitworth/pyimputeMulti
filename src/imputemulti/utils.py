"""Utility functions for data loading and preprocessing."""

import pathlib
from typing import Any, Dict, List
import itertools
import numpy as np
import pandas as pd

def load_tract2221() -> pd.DataFrame:
    """Load the tract2221 dataset from the root data directory."""
    path = pathlib.Path(__file__).parents[2] / "data" / "tract2221.parquet"
    return pd.read_parquet(path)


def expand_grid(levels_dict: Dict[str, List[Any]]) -> pd.DataFrame:
    """Perform a Python equivalent of R's expand.grid."""
    keys = levels_dict.keys()
    values = levels_dict.values()
    grid = list(itertools.product(*values))
    return pd.DataFrame(grid, columns=keys)


def fact_to_int(df: pd.DataFrame) -> np.ndarray:
    """Convert a dataframe with categorical columns to an integer array.

    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)
    
    for i, col in enumerate(df.columns):
        series = df[col]
        if not isinstance(series.dtype, pd.CategoricalDtype):
            series = series.astype('category')
        
        # codes are 0-indexed, R's are 1-indexed.
        # codes -1 represent NaN in pandas categorical.
        codes = series.cat.codes.values.astype(np.int32)
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes
        
    return out


def get_levels(df: pd.DataFrame) -> Dict[str, List[Any]]:
    """Get levels for each categorical column."""
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(df[col].astype('category').cat.categories)
    return levels
