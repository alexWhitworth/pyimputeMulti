"""Multivariate Multinomial Data Imputation.

This package provides functionalities for multivariate multinomial data imputation
using Expectation-Maximization (EM) and Data Augmentation (DA) algorithms.
"""

from .algorithms import multinomial_impute, multinomial_stats
from .utils import load_tract2221
from .models import ImputeMultiResult, ModImputeMultiResult

__all__ = [
    "multinomial_impute",
    "multinomial_stats",
    "load_tract2221",
    "ImputeMultiResult",
    "ModImputeMultiResult",
]
