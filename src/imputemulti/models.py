"""Data models for imputation results."""

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class ModImputeMultiResult:
    """Represents the estimated model parameters from EM or Data Augmentation."""

    method: str
    mle_call: str
    mle_iter: int
    mle_log_lik: float
    mle_cp: str
    mle_x_y: pd.DataFrame


@dataclass(frozen=True)
class ImputeMultiResult(ModImputeMultiResult):
    """Represents the outcome of a full imputation, including imputed data."""

    Gcall: str
    data: list[pd.DataFrame]
    nmiss: int
