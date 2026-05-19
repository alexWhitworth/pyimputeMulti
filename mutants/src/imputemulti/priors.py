import pandas as pd
import numpy as np
from typing import Optional, Union, Literal
from .utils import expand_grid, fact_to_int, get_levels
from ._internal_rust import count_compare_rust
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
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

def count_levels(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    args = [dat, enum_list, has_na]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_count_levels__mutmut_orig, x_count_levels__mutmut_mutants, args, kwargs, None)

def x_count_levels__mutmut_orig(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_1(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = None
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_2(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(None)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_3(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = None
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_4(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(None)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_5(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = None
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_6(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(None, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_7(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, None, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_8(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, None)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_9(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_10(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_11(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, )
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_12(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = None
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_13(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = None
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_14(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['XXcountsXX'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_15(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['COUNTS'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_16(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=None)

def x_count_levels__mutmut_17(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['XXcountsXX'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_18(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['COUNTS'] > 0].reset_index(drop=True)

def x_count_levels__mutmut_19(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] >= 0].reset_index(drop=True)

def x_count_levels__mutmut_20(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 1].reset_index(drop=True)

def x_count_levels__mutmut_21(dat: pd.DataFrame, enum_list: pd.DataFrame, 
                 has_na: Literal["no", "count.obs", "count.miss"]) -> pd.DataFrame:
    """
    Count occurrences of patterns in dat matching enum_list.
    """
    # convert to integers
    e2 = fact_to_int(enum_list)
    dat2 = fact_to_int(dat)
    
    # get counts from Rust
    counts = count_compare_rust(e2, dat2, has_na)
    
    enum_res = enum_list.copy()
    enum_res['counts'] = counts
    
    # Return only rows with counts > 0 (as in R)
    return enum_res[enum_res['counts'] > 0].reset_index(drop=False)

x_count_levels__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_count_levels__mutmut_1': x_count_levels__mutmut_1, 
    'x_count_levels__mutmut_2': x_count_levels__mutmut_2, 
    'x_count_levels__mutmut_3': x_count_levels__mutmut_3, 
    'x_count_levels__mutmut_4': x_count_levels__mutmut_4, 
    'x_count_levels__mutmut_5': x_count_levels__mutmut_5, 
    'x_count_levels__mutmut_6': x_count_levels__mutmut_6, 
    'x_count_levels__mutmut_7': x_count_levels__mutmut_7, 
    'x_count_levels__mutmut_8': x_count_levels__mutmut_8, 
    'x_count_levels__mutmut_9': x_count_levels__mutmut_9, 
    'x_count_levels__mutmut_10': x_count_levels__mutmut_10, 
    'x_count_levels__mutmut_11': x_count_levels__mutmut_11, 
    'x_count_levels__mutmut_12': x_count_levels__mutmut_12, 
    'x_count_levels__mutmut_13': x_count_levels__mutmut_13, 
    'x_count_levels__mutmut_14': x_count_levels__mutmut_14, 
    'x_count_levels__mutmut_15': x_count_levels__mutmut_15, 
    'x_count_levels__mutmut_16': x_count_levels__mutmut_16, 
    'x_count_levels__mutmut_17': x_count_levels__mutmut_17, 
    'x_count_levels__mutmut_18': x_count_levels__mutmut_18, 
    'x_count_levels__mutmut_19': x_count_levels__mutmut_19, 
    'x_count_levels__mutmut_20': x_count_levels__mutmut_20, 
    'x_count_levels__mutmut_21': x_count_levels__mutmut_21
}
x_count_levels__mutmut_orig.__name__ = 'x_count_levels'

def data_dep_prior_multi(dat: pd.DataFrame) -> pd.DataFrame:
    args = [dat]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_data_dep_prior_multi__mutmut_orig, x_data_dep_prior_multi__mutmut_mutants, args, kwargs, None)

def x_data_dep_prior_multi__mutmut_orig(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_1(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = None
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_2(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(None)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_3(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = None
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_4(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(None)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_5(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = None
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_6(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=None)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_7(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=2)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_8(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = None
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_9(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(None)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_10(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[1]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_11(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = None
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_12(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) * len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_13(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac <= 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_14(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 1.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_15(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = None
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_16(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(None, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_17(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, None, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_18(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na=None)
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_19(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_20(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_21(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, )
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_22(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="XXnoXX")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_23(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="NO")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_24(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = None
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_25(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(None)
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_26(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(None))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_27(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 / len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_28(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(1.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_29(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = None
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_30(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(None, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_31(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=None, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_32(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=None)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_33(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_34(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_35(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, )
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_36(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=False)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_37(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = None
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_38(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(None, enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_39(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], None, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_40(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na=None)
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_41(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_42(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_43(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, )
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_44(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="XXnoXX")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_45(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="NO")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_46(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = None
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_47(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(None, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_48(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, None, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_49(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=None, how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_50(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how=None)
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_51(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_52(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_53(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_54(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), )
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_55(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(None), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_56(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='XXleftXX')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_57(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='LEFT')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_58(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = None
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_59(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['XXcountsXX'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_60(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['COUNTS'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_61(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(None)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_62(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(None).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_63(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['XXcountsXX'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_64(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['COUNTS'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_65(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(2).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_66(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns=None, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_67(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=None)
    
    return prior

def x_data_dep_prior_multi__mutmut_68(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_69(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, )
    
    return prior

def x_data_dep_prior_multi__mutmut_70(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'XXcountsXX': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_71(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'COUNTS': 'alpha'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_72(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'XXalphaXX'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_73(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'ALPHA'}, inplace=True)
    
    return prior

def x_data_dep_prior_multi__mutmut_74(dat: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a data dependent prior for p-dimensional multinomial distributions.
    """
    levels = get_levels(dat)
    enum = expand_grid(levels)
    
    comp_mask = dat.notna().all(axis=1)
    comp_indices = np.where(comp_mask)[0]
    comp_frac = len(comp_indices) / len(dat)
    
    if comp_frac < 0.2:
        prior_counts = count_levels(dat, enum, has_na="no")
    else:
        n = int(round(0.2 * len(dat)))
        samp_indices = np.random.choice(comp_indices, size=n, replace=True)
        prior_counts = count_levels(dat.iloc[samp_indices], enum, has_na="no")
    
    # Merge with enum to ensure all patterns are present
    prior = pd.merge(enum, prior_counts, on=list(enum.columns), how='left')
    prior['counts'] = prior['counts'].fillna(1).astype(np.float64)
    prior.rename(columns={'counts': 'alpha'}, inplace=False)
    
    return prior

x_data_dep_prior_multi__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_data_dep_prior_multi__mutmut_1': x_data_dep_prior_multi__mutmut_1, 
    'x_data_dep_prior_multi__mutmut_2': x_data_dep_prior_multi__mutmut_2, 
    'x_data_dep_prior_multi__mutmut_3': x_data_dep_prior_multi__mutmut_3, 
    'x_data_dep_prior_multi__mutmut_4': x_data_dep_prior_multi__mutmut_4, 
    'x_data_dep_prior_multi__mutmut_5': x_data_dep_prior_multi__mutmut_5, 
    'x_data_dep_prior_multi__mutmut_6': x_data_dep_prior_multi__mutmut_6, 
    'x_data_dep_prior_multi__mutmut_7': x_data_dep_prior_multi__mutmut_7, 
    'x_data_dep_prior_multi__mutmut_8': x_data_dep_prior_multi__mutmut_8, 
    'x_data_dep_prior_multi__mutmut_9': x_data_dep_prior_multi__mutmut_9, 
    'x_data_dep_prior_multi__mutmut_10': x_data_dep_prior_multi__mutmut_10, 
    'x_data_dep_prior_multi__mutmut_11': x_data_dep_prior_multi__mutmut_11, 
    'x_data_dep_prior_multi__mutmut_12': x_data_dep_prior_multi__mutmut_12, 
    'x_data_dep_prior_multi__mutmut_13': x_data_dep_prior_multi__mutmut_13, 
    'x_data_dep_prior_multi__mutmut_14': x_data_dep_prior_multi__mutmut_14, 
    'x_data_dep_prior_multi__mutmut_15': x_data_dep_prior_multi__mutmut_15, 
    'x_data_dep_prior_multi__mutmut_16': x_data_dep_prior_multi__mutmut_16, 
    'x_data_dep_prior_multi__mutmut_17': x_data_dep_prior_multi__mutmut_17, 
    'x_data_dep_prior_multi__mutmut_18': x_data_dep_prior_multi__mutmut_18, 
    'x_data_dep_prior_multi__mutmut_19': x_data_dep_prior_multi__mutmut_19, 
    'x_data_dep_prior_multi__mutmut_20': x_data_dep_prior_multi__mutmut_20, 
    'x_data_dep_prior_multi__mutmut_21': x_data_dep_prior_multi__mutmut_21, 
    'x_data_dep_prior_multi__mutmut_22': x_data_dep_prior_multi__mutmut_22, 
    'x_data_dep_prior_multi__mutmut_23': x_data_dep_prior_multi__mutmut_23, 
    'x_data_dep_prior_multi__mutmut_24': x_data_dep_prior_multi__mutmut_24, 
    'x_data_dep_prior_multi__mutmut_25': x_data_dep_prior_multi__mutmut_25, 
    'x_data_dep_prior_multi__mutmut_26': x_data_dep_prior_multi__mutmut_26, 
    'x_data_dep_prior_multi__mutmut_27': x_data_dep_prior_multi__mutmut_27, 
    'x_data_dep_prior_multi__mutmut_28': x_data_dep_prior_multi__mutmut_28, 
    'x_data_dep_prior_multi__mutmut_29': x_data_dep_prior_multi__mutmut_29, 
    'x_data_dep_prior_multi__mutmut_30': x_data_dep_prior_multi__mutmut_30, 
    'x_data_dep_prior_multi__mutmut_31': x_data_dep_prior_multi__mutmut_31, 
    'x_data_dep_prior_multi__mutmut_32': x_data_dep_prior_multi__mutmut_32, 
    'x_data_dep_prior_multi__mutmut_33': x_data_dep_prior_multi__mutmut_33, 
    'x_data_dep_prior_multi__mutmut_34': x_data_dep_prior_multi__mutmut_34, 
    'x_data_dep_prior_multi__mutmut_35': x_data_dep_prior_multi__mutmut_35, 
    'x_data_dep_prior_multi__mutmut_36': x_data_dep_prior_multi__mutmut_36, 
    'x_data_dep_prior_multi__mutmut_37': x_data_dep_prior_multi__mutmut_37, 
    'x_data_dep_prior_multi__mutmut_38': x_data_dep_prior_multi__mutmut_38, 
    'x_data_dep_prior_multi__mutmut_39': x_data_dep_prior_multi__mutmut_39, 
    'x_data_dep_prior_multi__mutmut_40': x_data_dep_prior_multi__mutmut_40, 
    'x_data_dep_prior_multi__mutmut_41': x_data_dep_prior_multi__mutmut_41, 
    'x_data_dep_prior_multi__mutmut_42': x_data_dep_prior_multi__mutmut_42, 
    'x_data_dep_prior_multi__mutmut_43': x_data_dep_prior_multi__mutmut_43, 
    'x_data_dep_prior_multi__mutmut_44': x_data_dep_prior_multi__mutmut_44, 
    'x_data_dep_prior_multi__mutmut_45': x_data_dep_prior_multi__mutmut_45, 
    'x_data_dep_prior_multi__mutmut_46': x_data_dep_prior_multi__mutmut_46, 
    'x_data_dep_prior_multi__mutmut_47': x_data_dep_prior_multi__mutmut_47, 
    'x_data_dep_prior_multi__mutmut_48': x_data_dep_prior_multi__mutmut_48, 
    'x_data_dep_prior_multi__mutmut_49': x_data_dep_prior_multi__mutmut_49, 
    'x_data_dep_prior_multi__mutmut_50': x_data_dep_prior_multi__mutmut_50, 
    'x_data_dep_prior_multi__mutmut_51': x_data_dep_prior_multi__mutmut_51, 
    'x_data_dep_prior_multi__mutmut_52': x_data_dep_prior_multi__mutmut_52, 
    'x_data_dep_prior_multi__mutmut_53': x_data_dep_prior_multi__mutmut_53, 
    'x_data_dep_prior_multi__mutmut_54': x_data_dep_prior_multi__mutmut_54, 
    'x_data_dep_prior_multi__mutmut_55': x_data_dep_prior_multi__mutmut_55, 
    'x_data_dep_prior_multi__mutmut_56': x_data_dep_prior_multi__mutmut_56, 
    'x_data_dep_prior_multi__mutmut_57': x_data_dep_prior_multi__mutmut_57, 
    'x_data_dep_prior_multi__mutmut_58': x_data_dep_prior_multi__mutmut_58, 
    'x_data_dep_prior_multi__mutmut_59': x_data_dep_prior_multi__mutmut_59, 
    'x_data_dep_prior_multi__mutmut_60': x_data_dep_prior_multi__mutmut_60, 
    'x_data_dep_prior_multi__mutmut_61': x_data_dep_prior_multi__mutmut_61, 
    'x_data_dep_prior_multi__mutmut_62': x_data_dep_prior_multi__mutmut_62, 
    'x_data_dep_prior_multi__mutmut_63': x_data_dep_prior_multi__mutmut_63, 
    'x_data_dep_prior_multi__mutmut_64': x_data_dep_prior_multi__mutmut_64, 
    'x_data_dep_prior_multi__mutmut_65': x_data_dep_prior_multi__mutmut_65, 
    'x_data_dep_prior_multi__mutmut_66': x_data_dep_prior_multi__mutmut_66, 
    'x_data_dep_prior_multi__mutmut_67': x_data_dep_prior_multi__mutmut_67, 
    'x_data_dep_prior_multi__mutmut_68': x_data_dep_prior_multi__mutmut_68, 
    'x_data_dep_prior_multi__mutmut_69': x_data_dep_prior_multi__mutmut_69, 
    'x_data_dep_prior_multi__mutmut_70': x_data_dep_prior_multi__mutmut_70, 
    'x_data_dep_prior_multi__mutmut_71': x_data_dep_prior_multi__mutmut_71, 
    'x_data_dep_prior_multi__mutmut_72': x_data_dep_prior_multi__mutmut_72, 
    'x_data_dep_prior_multi__mutmut_73': x_data_dep_prior_multi__mutmut_73, 
    'x_data_dep_prior_multi__mutmut_74': x_data_dep_prior_multi__mutmut_74
}
x_data_dep_prior_multi__mutmut_orig.__name__ = 'x_data_dep_prior_multi'

def check_prior(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    args = [dat, conj_prior, alpha, verbose, outer, enum_comp]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check_prior__mutmut_orig, x_check_prior__mutmut_mutants, args, kwargs, None)

def x_check_prior__mutmut_orig(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_1(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "XXnoneXX",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_2(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "NONE",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_3(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = True,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_4(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = True,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_5(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior != "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_6(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "XXnoneXX":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_7(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "NONE":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_8(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior != "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_9(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "XXdata.depXX":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_10(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "DATA.DEP":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_11(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_12(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print(None)
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_13(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("XXUsing user-supplied data dependent prior.XX")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_14(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_15(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("USING USER-SUPPLIED DATA DEPENDENT PRIOR.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_16(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print(None)
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_17(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("XXCalculating data dependent prior.XX")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_18(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_19(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("CALCULATING DATA DEPENDENT PRIOR.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_20(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(None)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_21(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior != "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_22(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "XXflat.priorXX":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_23(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "FLAT.PRIOR":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_24(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_25(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError(None)
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_26(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("XXFlat priors must be supplied as a scalar.XX")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_27(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_28(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("FLAT PRIORS MUST BE SUPPLIED AS A SCALAR.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_29(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior != "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_30(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "XXnon.informativeXX":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_31(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "NON.INFORMATIVE":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_32(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 2.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_33(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is not None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_34(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError(None)
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_35(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("XXenum_comp must be provided if outer=FalseXX")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_36(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=false")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_37(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("ENUM_COMP MUST BE PROVIDED IF OUTER=FALSE")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_38(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = None
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_39(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior == "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_40(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "XXnoneXX":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_41(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "NONE":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_42(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior != "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_43(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "XXdata.depXX":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_44(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "DATA.DEP":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_45(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_46(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError(None)
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_47(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("XXalpha must be a DataFrame for data.dep priorXX")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_48(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a dataframe for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_49(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("ALPHA MUST BE A DATAFRAME FOR DATA.DEP PRIOR")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_50(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) == len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_51(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError(None)
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_52(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("XXlen(alpha) must match len(enum_comp)XX")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_53(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("LEN(ALPHA) MUST MATCH LEN(ENUM_COMP)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_54(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = None
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_55(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(None, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_56(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, None, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_57(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=None)
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_58(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_59(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_60(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, )
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_61(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(None))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_62(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior != "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_63(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "XXflat.priorXX":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_64(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "FLAT.PRIOR":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_65(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_66(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError(None)
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_67(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("XXFlat priors must be supplied as a scalar.XX")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_68(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_69(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("FLAT PRIORS MUST BE SUPPLIED AS A SCALAR.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_70(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = None
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_71(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['XXalphaXX'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_72(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['ALPHA'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_73(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior != "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_74(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "XXnon.informativeXX":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_75(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "NON.INFORMATIVE":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_76(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = None
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_77(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['XXalphaXX'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_78(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['ALPHA'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_79(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 2.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_80(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = None
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_81(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['XXtheta_yXX'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_82(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['THETA_Y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_83(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] * res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_84(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['XXalphaXX'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_85(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['ALPHA'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_86(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['XXalphaXX'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_87(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['ALPHA'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_88(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = None
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_89(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['XXtheta_yXX'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_90(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['THETA_Y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_91(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=None)
            res['theta_y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_92(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] = res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_93(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] *= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_94(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['XXtheta_yXX'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_95(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['THETA_Y'] /= res['theta_y'].sum()
            
        return res

def x_check_prior__mutmut_96(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['XXtheta_yXX'].sum()
            
        return res

def x_check_prior__mutmut_97(dat: pd.DataFrame, 
                conj_prior: Literal["none", "data.dep", "flat.prior", "non.informative"] = "none",
                alpha: Optional[Union[float, pd.DataFrame]] = None,
                verbose: bool = False,
                outer: bool = False,
                enum_comp: Optional[pd.DataFrame] = None) -> Optional[Union[float, pd.DataFrame]]:
    """
    Helper function for checking priors.
    """
    if outer:
        if conj_prior == "none":
            return None
        
        if conj_prior == "data.dep":
            if alpha is not None:
                if verbose:
                    print("Using user-supplied data dependent prior.")
                return alpha
            else:
                if verbose:
                    print("Calculating data dependent prior.")
                return data_dep_prior_multi(dat)
        elif conj_prior == "flat.prior":
            if not isinstance(alpha, (int, float)):
                raise ValueError("Flat priors must be supplied as a scalar.")
            return alpha
        elif conj_prior == "non.informative":
            return 1.0
        return None
    else:
        # called within EM or DA
        if enum_comp is None:
            raise ValueError("enum_comp must be provided if outer=False")
            
        res = enum_comp.copy()
        if conj_prior != "none":
            if conj_prior == "data.dep":
                if not isinstance(alpha, pd.DataFrame):
                    raise ValueError("alpha must be a DataFrame for data.dep prior")
                if len(alpha) != len(res):
                    raise ValueError("len(alpha) must match len(enum_comp)")
                # Merge alpha into res
                res = pd.merge(res, alpha, on=list(dat.columns))
            elif conj_prior == "flat.prior":
                if not isinstance(alpha, (int, float)):
                    raise ValueError("Flat priors must be supplied as a scalar.")
                res['alpha'] = alpha
            elif conj_prior == "non.informative":
                res['alpha'] = 1.0
            
            res['theta_y'] = res['alpha'] / res['alpha'].sum()
        else:
            # random initialization
            res['theta_y'] = np.random.uniform(size=len(res))
            res['theta_y'] /= res['THETA_Y'].sum()
            
        return res

x_check_prior__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_check_prior__mutmut_1': x_check_prior__mutmut_1, 
    'x_check_prior__mutmut_2': x_check_prior__mutmut_2, 
    'x_check_prior__mutmut_3': x_check_prior__mutmut_3, 
    'x_check_prior__mutmut_4': x_check_prior__mutmut_4, 
    'x_check_prior__mutmut_5': x_check_prior__mutmut_5, 
    'x_check_prior__mutmut_6': x_check_prior__mutmut_6, 
    'x_check_prior__mutmut_7': x_check_prior__mutmut_7, 
    'x_check_prior__mutmut_8': x_check_prior__mutmut_8, 
    'x_check_prior__mutmut_9': x_check_prior__mutmut_9, 
    'x_check_prior__mutmut_10': x_check_prior__mutmut_10, 
    'x_check_prior__mutmut_11': x_check_prior__mutmut_11, 
    'x_check_prior__mutmut_12': x_check_prior__mutmut_12, 
    'x_check_prior__mutmut_13': x_check_prior__mutmut_13, 
    'x_check_prior__mutmut_14': x_check_prior__mutmut_14, 
    'x_check_prior__mutmut_15': x_check_prior__mutmut_15, 
    'x_check_prior__mutmut_16': x_check_prior__mutmut_16, 
    'x_check_prior__mutmut_17': x_check_prior__mutmut_17, 
    'x_check_prior__mutmut_18': x_check_prior__mutmut_18, 
    'x_check_prior__mutmut_19': x_check_prior__mutmut_19, 
    'x_check_prior__mutmut_20': x_check_prior__mutmut_20, 
    'x_check_prior__mutmut_21': x_check_prior__mutmut_21, 
    'x_check_prior__mutmut_22': x_check_prior__mutmut_22, 
    'x_check_prior__mutmut_23': x_check_prior__mutmut_23, 
    'x_check_prior__mutmut_24': x_check_prior__mutmut_24, 
    'x_check_prior__mutmut_25': x_check_prior__mutmut_25, 
    'x_check_prior__mutmut_26': x_check_prior__mutmut_26, 
    'x_check_prior__mutmut_27': x_check_prior__mutmut_27, 
    'x_check_prior__mutmut_28': x_check_prior__mutmut_28, 
    'x_check_prior__mutmut_29': x_check_prior__mutmut_29, 
    'x_check_prior__mutmut_30': x_check_prior__mutmut_30, 
    'x_check_prior__mutmut_31': x_check_prior__mutmut_31, 
    'x_check_prior__mutmut_32': x_check_prior__mutmut_32, 
    'x_check_prior__mutmut_33': x_check_prior__mutmut_33, 
    'x_check_prior__mutmut_34': x_check_prior__mutmut_34, 
    'x_check_prior__mutmut_35': x_check_prior__mutmut_35, 
    'x_check_prior__mutmut_36': x_check_prior__mutmut_36, 
    'x_check_prior__mutmut_37': x_check_prior__mutmut_37, 
    'x_check_prior__mutmut_38': x_check_prior__mutmut_38, 
    'x_check_prior__mutmut_39': x_check_prior__mutmut_39, 
    'x_check_prior__mutmut_40': x_check_prior__mutmut_40, 
    'x_check_prior__mutmut_41': x_check_prior__mutmut_41, 
    'x_check_prior__mutmut_42': x_check_prior__mutmut_42, 
    'x_check_prior__mutmut_43': x_check_prior__mutmut_43, 
    'x_check_prior__mutmut_44': x_check_prior__mutmut_44, 
    'x_check_prior__mutmut_45': x_check_prior__mutmut_45, 
    'x_check_prior__mutmut_46': x_check_prior__mutmut_46, 
    'x_check_prior__mutmut_47': x_check_prior__mutmut_47, 
    'x_check_prior__mutmut_48': x_check_prior__mutmut_48, 
    'x_check_prior__mutmut_49': x_check_prior__mutmut_49, 
    'x_check_prior__mutmut_50': x_check_prior__mutmut_50, 
    'x_check_prior__mutmut_51': x_check_prior__mutmut_51, 
    'x_check_prior__mutmut_52': x_check_prior__mutmut_52, 
    'x_check_prior__mutmut_53': x_check_prior__mutmut_53, 
    'x_check_prior__mutmut_54': x_check_prior__mutmut_54, 
    'x_check_prior__mutmut_55': x_check_prior__mutmut_55, 
    'x_check_prior__mutmut_56': x_check_prior__mutmut_56, 
    'x_check_prior__mutmut_57': x_check_prior__mutmut_57, 
    'x_check_prior__mutmut_58': x_check_prior__mutmut_58, 
    'x_check_prior__mutmut_59': x_check_prior__mutmut_59, 
    'x_check_prior__mutmut_60': x_check_prior__mutmut_60, 
    'x_check_prior__mutmut_61': x_check_prior__mutmut_61, 
    'x_check_prior__mutmut_62': x_check_prior__mutmut_62, 
    'x_check_prior__mutmut_63': x_check_prior__mutmut_63, 
    'x_check_prior__mutmut_64': x_check_prior__mutmut_64, 
    'x_check_prior__mutmut_65': x_check_prior__mutmut_65, 
    'x_check_prior__mutmut_66': x_check_prior__mutmut_66, 
    'x_check_prior__mutmut_67': x_check_prior__mutmut_67, 
    'x_check_prior__mutmut_68': x_check_prior__mutmut_68, 
    'x_check_prior__mutmut_69': x_check_prior__mutmut_69, 
    'x_check_prior__mutmut_70': x_check_prior__mutmut_70, 
    'x_check_prior__mutmut_71': x_check_prior__mutmut_71, 
    'x_check_prior__mutmut_72': x_check_prior__mutmut_72, 
    'x_check_prior__mutmut_73': x_check_prior__mutmut_73, 
    'x_check_prior__mutmut_74': x_check_prior__mutmut_74, 
    'x_check_prior__mutmut_75': x_check_prior__mutmut_75, 
    'x_check_prior__mutmut_76': x_check_prior__mutmut_76, 
    'x_check_prior__mutmut_77': x_check_prior__mutmut_77, 
    'x_check_prior__mutmut_78': x_check_prior__mutmut_78, 
    'x_check_prior__mutmut_79': x_check_prior__mutmut_79, 
    'x_check_prior__mutmut_80': x_check_prior__mutmut_80, 
    'x_check_prior__mutmut_81': x_check_prior__mutmut_81, 
    'x_check_prior__mutmut_82': x_check_prior__mutmut_82, 
    'x_check_prior__mutmut_83': x_check_prior__mutmut_83, 
    'x_check_prior__mutmut_84': x_check_prior__mutmut_84, 
    'x_check_prior__mutmut_85': x_check_prior__mutmut_85, 
    'x_check_prior__mutmut_86': x_check_prior__mutmut_86, 
    'x_check_prior__mutmut_87': x_check_prior__mutmut_87, 
    'x_check_prior__mutmut_88': x_check_prior__mutmut_88, 
    'x_check_prior__mutmut_89': x_check_prior__mutmut_89, 
    'x_check_prior__mutmut_90': x_check_prior__mutmut_90, 
    'x_check_prior__mutmut_91': x_check_prior__mutmut_91, 
    'x_check_prior__mutmut_92': x_check_prior__mutmut_92, 
    'x_check_prior__mutmut_93': x_check_prior__mutmut_93, 
    'x_check_prior__mutmut_94': x_check_prior__mutmut_94, 
    'x_check_prior__mutmut_95': x_check_prior__mutmut_95, 
    'x_check_prior__mutmut_96': x_check_prior__mutmut_96, 
    'x_check_prior__mutmut_97': x_check_prior__mutmut_97
}
x_check_prior__mutmut_orig.__name__ = 'x_check_prior'
