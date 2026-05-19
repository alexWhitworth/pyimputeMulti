import itertools
from collections.abc import Callable
from typing import Annotated, Any, ClassVar

import numpy as np
import pandas as pd

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os  # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException  # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit  # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

def expand_grid(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    args = [levels_dict]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_expand_grid__mutmut_orig, x_expand_grid__mutmut_mutants, args, kwargs, None)

def x_expand_grid__mutmut_orig(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = levels_dict.keys()
    values = levels_dict.values()
    grid = list(itertools.product(*values))
    return pd.DataFrame(grid, columns=keys)

def x_expand_grid__mutmut_1(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = None
    values = levels_dict.values()
    grid = list(itertools.product(*values))
    return pd.DataFrame(grid, columns=keys)

def x_expand_grid__mutmut_2(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = levels_dict.keys()
    values = None
    grid = list(itertools.product(*values))
    return pd.DataFrame(grid, columns=keys)

def x_expand_grid__mutmut_3(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = levels_dict.keys()
    levels_dict.values()
    grid = None
    return pd.DataFrame(grid, columns=keys)

def x_expand_grid__mutmut_4(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = levels_dict.keys()
    levels_dict.values()
    grid = list(None)
    return pd.DataFrame(grid, columns=keys)

def x_expand_grid__mutmut_5(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = levels_dict.keys()
    values = levels_dict.values()
    list(itertools.product(*values))
    return pd.DataFrame(None, columns=keys)

def x_expand_grid__mutmut_6(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    levels_dict.keys()
    values = levels_dict.values()
    grid = list(itertools.product(*values))
    return pd.DataFrame(grid, columns=None)

def x_expand_grid__mutmut_7(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    keys = levels_dict.keys()
    values = levels_dict.values()
    list(itertools.product(*values))
    return pd.DataFrame(columns=keys)

def x_expand_grid__mutmut_8(levels_dict: dict[str, list[Any]]) -> pd.DataFrame:
    """
    Python equivalent of R's expand.grid.
    """
    levels_dict.keys()
    values = levels_dict.values()
    grid = list(itertools.product(*values))
    return pd.DataFrame(grid, )

x_expand_grid__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_expand_grid__mutmut_1': x_expand_grid__mutmut_1,
    'x_expand_grid__mutmut_2': x_expand_grid__mutmut_2,
    'x_expand_grid__mutmut_3': x_expand_grid__mutmut_3,
    'x_expand_grid__mutmut_4': x_expand_grid__mutmut_4,
    'x_expand_grid__mutmut_5': x_expand_grid__mutmut_5,
    'x_expand_grid__mutmut_6': x_expand_grid__mutmut_6,
    'x_expand_grid__mutmut_7': x_expand_grid__mutmut_7,
    'x_expand_grid__mutmut_8': x_expand_grid__mutmut_8
}
x_expand_grid__mutmut_orig.__name__ = 'x_expand_grid'

def fact_to_int(df: pd.DataFrame) -> np.ndarray:
    args = [df]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_fact_to_int__mutmut_orig, x_fact_to_int__mutmut_mutants, args, kwargs, None)

def x_fact_to_int__mutmut_orig(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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

def x_fact_to_int__mutmut_1(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = None
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

def x_fact_to_int__mutmut_2(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(None)
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

def x_fact_to_int__mutmut_3(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(+2147483648)
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

def x_fact_to_int__mutmut_4(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483649)
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

def x_fact_to_int__mutmut_5(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = None

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

def x_fact_to_int__mutmut_6(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(None, dtype=np.int32)

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

def x_fact_to_int__mutmut_7(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=None)

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

def x_fact_to_int__mutmut_8(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(dtype=np.int32)

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

def x_fact_to_int__mutmut_9(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, )

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

def x_fact_to_int__mutmut_10(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, col in enumerate(None):
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

def x_fact_to_int__mutmut_11(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, _col in enumerate(df.columns):
        series = None
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

def x_fact_to_int__mutmut_12(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, col in enumerate(df.columns):
        series = df[col]
        if isinstance(series.dtype, pd.CategoricalDtype):
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

def x_fact_to_int__mutmut_13(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, col in enumerate(df.columns):
        series = df[col]
        if not isinstance(series.dtype, pd.CategoricalDtype):
            series = None

        # codes are 0-indexed, R's are 1-indexed.
        # codes -1 represent NaN in pandas categorical.
        codes = series.cat.codes.values.astype(np.int32)
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_14(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, col in enumerate(df.columns):
        series = df[col]
        if not isinstance(series.dtype, pd.CategoricalDtype):
            series = series.astype(None)

        # codes are 0-indexed, R's are 1-indexed.
        # codes -1 represent NaN in pandas categorical.
        codes = series.cat.codes.values.astype(np.int32)
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_15(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, col in enumerate(df.columns):
        series = df[col]
        if not isinstance(series.dtype, pd.CategoricalDtype):
            series = series.astype('XXcategoryXX')

        # codes are 0-indexed, R's are 1-indexed.
        # codes -1 represent NaN in pandas categorical.
        codes = series.cat.codes.values.astype(np.int32)
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_16(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    NA_VAL = np.int32(-2147483648)
    out = np.zeros(df.shape, dtype=np.int32)

    for i, col in enumerate(df.columns):
        series = df[col]
        if not isinstance(series.dtype, pd.CategoricalDtype):
            series = series.astype('CATEGORY')

        # codes are 0-indexed, R's are 1-indexed.
        # codes -1 represent NaN in pandas categorical.
        codes = series.cat.codes.values.astype(np.int32)
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_17(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        codes = None
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_18(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        codes = series.cat.codes.values.astype(None)
        # Convert to 1-indexed and handle NaNs
        mask = codes == -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_19(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        mask = None
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_20(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        mask = codes != -1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_21(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        mask = codes == +1
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_22(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        mask = codes == -2
        codes = codes + 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_23(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        codes = None
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_24(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        codes = codes - 1
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_25(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        codes = codes + 2
        codes[mask] = NA_VAL
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_26(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
    Missing values are represented as i32::MIN (-2147483648).
    """
    np.int32(-2147483648)
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
        codes[mask] = None
        out[:, i] = codes

    return out

def x_fact_to_int__mutmut_27(df: pd.DataFrame) -> np.ndarray:
    """
    Convert a dataframe with categorical columns to an integer array.
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
        out[:, i] = None

    return out

x_fact_to_int__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_fact_to_int__mutmut_1': x_fact_to_int__mutmut_1,
    'x_fact_to_int__mutmut_2': x_fact_to_int__mutmut_2,
    'x_fact_to_int__mutmut_3': x_fact_to_int__mutmut_3,
    'x_fact_to_int__mutmut_4': x_fact_to_int__mutmut_4,
    'x_fact_to_int__mutmut_5': x_fact_to_int__mutmut_5,
    'x_fact_to_int__mutmut_6': x_fact_to_int__mutmut_6,
    'x_fact_to_int__mutmut_7': x_fact_to_int__mutmut_7,
    'x_fact_to_int__mutmut_8': x_fact_to_int__mutmut_8,
    'x_fact_to_int__mutmut_9': x_fact_to_int__mutmut_9,
    'x_fact_to_int__mutmut_10': x_fact_to_int__mutmut_10,
    'x_fact_to_int__mutmut_11': x_fact_to_int__mutmut_11,
    'x_fact_to_int__mutmut_12': x_fact_to_int__mutmut_12,
    'x_fact_to_int__mutmut_13': x_fact_to_int__mutmut_13,
    'x_fact_to_int__mutmut_14': x_fact_to_int__mutmut_14,
    'x_fact_to_int__mutmut_15': x_fact_to_int__mutmut_15,
    'x_fact_to_int__mutmut_16': x_fact_to_int__mutmut_16,
    'x_fact_to_int__mutmut_17': x_fact_to_int__mutmut_17,
    'x_fact_to_int__mutmut_18': x_fact_to_int__mutmut_18,
    'x_fact_to_int__mutmut_19': x_fact_to_int__mutmut_19,
    'x_fact_to_int__mutmut_20': x_fact_to_int__mutmut_20,
    'x_fact_to_int__mutmut_21': x_fact_to_int__mutmut_21,
    'x_fact_to_int__mutmut_22': x_fact_to_int__mutmut_22,
    'x_fact_to_int__mutmut_23': x_fact_to_int__mutmut_23,
    'x_fact_to_int__mutmut_24': x_fact_to_int__mutmut_24,
    'x_fact_to_int__mutmut_25': x_fact_to_int__mutmut_25,
    'x_fact_to_int__mutmut_26': x_fact_to_int__mutmut_26,
    'x_fact_to_int__mutmut_27': x_fact_to_int__mutmut_27
}
x_fact_to_int__mutmut_orig.__name__ = 'x_fact_to_int'

def get_levels(df: pd.DataFrame) -> dict[str, list[Any]]:
    args = [df]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_levels__mutmut_orig, x_get_levels__mutmut_mutants, args, kwargs, None)

def x_get_levels__mutmut_orig(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(df[col].astype('category').cat.categories)
    return levels

def x_get_levels__mutmut_1(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = None
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(df[col].astype('category').cat.categories)
    return levels

def x_get_levels__mutmut_2(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = None
        else:
            levels[col] = list(df[col].astype('category').cat.categories)
    return levels

def x_get_levels__mutmut_3(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(None)
        else:
            levels[col] = list(df[col].astype('category').cat.categories)
    return levels

def x_get_levels__mutmut_4(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = None
    return levels

def x_get_levels__mutmut_5(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(None)
    return levels

def x_get_levels__mutmut_6(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(df[col].astype(None).cat.categories)
    return levels

def x_get_levels__mutmut_7(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(df[col].astype('XXcategoryXX').cat.categories)
    return levels

def x_get_levels__mutmut_8(df: pd.DataFrame) -> dict[str, list[Any]]:
    """
    Get levels for each categorical column.
    """
    levels = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            levels[col] = list(df[col].cat.categories)
        else:
            levels[col] = list(df[col].astype('CATEGORY').cat.categories)
    return levels

x_get_levels__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_levels__mutmut_1': x_get_levels__mutmut_1,
    'x_get_levels__mutmut_2': x_get_levels__mutmut_2,
    'x_get_levels__mutmut_3': x_get_levels__mutmut_3,
    'x_get_levels__mutmut_4': x_get_levels__mutmut_4,
    'x_get_levels__mutmut_5': x_get_levels__mutmut_5,
    'x_get_levels__mutmut_6': x_get_levels__mutmut_6,
    'x_get_levels__mutmut_7': x_get_levels__mutmut_7,
    'x_get_levels__mutmut_8': x_get_levels__mutmut_8
}
x_get_levels__mutmut_orig.__name__ = 'x_get_levels'
