# Stub file for imputemulti._internal_rust


import numpy as np

# Type aliases for clarity, inferred from spec.json api_contracts
PyReadonlyArray2_i32 = np.ndarray[tuple[int, int], np.dtype[np.int32]]
PyReadonlyArray1_f64 = np.ndarray[tuple[int], np.dtype[np.float64]]
PyArray1_i32 = np.ndarray[tuple[int], np.dtype[np.int32]]

def count_compare_rust(
    x: PyReadonlyArray2_i32, dat: PyReadonlyArray2_i32, has_na: str
) -> PyArray1_i32: ...
def sup_dist_c_rust(x: PyReadonlyArray1_f64, y: PyReadonlyArray1_f64) -> float: ...
def mx_my_compare_rust(
    mat_x: PyReadonlyArray2_i32, mat_y: PyReadonlyArray2_i32
) -> list[list[int]]: ...
