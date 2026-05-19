import pandas as pd
from importlib import resources
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

def load_tract2221() -> pd.DataFrame:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_load_tract2221__mutmut_orig, x_load_tract2221__mutmut_mutants, args, kwargs, None)

def x_load_tract2221__mutmut_orig() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("imputemulti.data").joinpath("tract2221.parquet")
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_1() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = None
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_2() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("imputemulti.data").joinpath(None)
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_3() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files(None).joinpath("tract2221.parquet")
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_4() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("XXimputemulti.dataXX").joinpath("tract2221.parquet")
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_5() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("IMPUTEMULTI.DATA").joinpath("tract2221.parquet")
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_6() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("imputemulti.data").joinpath("XXtract2221.parquetXX")
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_7() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("imputemulti.data").joinpath("TRACT2221.PARQUET")
    return pd.read_parquet(path)

def x_load_tract2221__mutmut_8() -> pd.DataFrame:
    """
    Load the tract2221 dataset.
    
    Returns:
        pd.DataFrame: The tract2221 dataset.
    """
    path = resources.files("imputemulti.data").joinpath("tract2221.parquet")
    return pd.read_parquet(None)

x_load_tract2221__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_load_tract2221__mutmut_1': x_load_tract2221__mutmut_1, 
    'x_load_tract2221__mutmut_2': x_load_tract2221__mutmut_2, 
    'x_load_tract2221__mutmut_3': x_load_tract2221__mutmut_3, 
    'x_load_tract2221__mutmut_4': x_load_tract2221__mutmut_4, 
    'x_load_tract2221__mutmut_5': x_load_tract2221__mutmut_5, 
    'x_load_tract2221__mutmut_6': x_load_tract2221__mutmut_6, 
    'x_load_tract2221__mutmut_7': x_load_tract2221__mutmut_7, 
    'x_load_tract2221__mutmut_8': x_load_tract2221__mutmut_8
}
x_load_tract2221__mutmut_orig.__name__ = 'x_load_tract2221'
