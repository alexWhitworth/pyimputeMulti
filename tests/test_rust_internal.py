import numpy as np
import pytest
from imputemulti._internal_rust import sup_dist_c_rust, count_compare_rust, mx_my_compare_rust

def test_sup_dist_c_rust():
    x = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    y = np.array([1.1, 1.9, 3.5], dtype=np.float64)
    # max abs diff is 0.5
    assert pytest.approx(sup_dist_c_rust(x, y)) == 0.5

def test_count_compare_rust_no_na():
    x = np.array([[1, 2], [3, 4]], dtype=np.int32)
    dat = np.array([[1, 2], [1, 2], [3, 4]], dtype=np.int32)
    counts = count_compare_rust(x, dat, "no")
    np.testing.assert_array_equal(counts, [2, 1])

def test_count_compare_rust_count_obs():
    # NA_INTEGER is i32::MIN
    NA = np.int32(-2147483648)
    x = np.array([[1, 2], [3, 4]], dtype=np.int32)
    dat = np.array([[1, NA], [3, 4], [NA, 2]], dtype=np.int32)
    # [1, NA] matches [1, 2]
    # [3, 4] matches [3, 4]
    # [NA, 2] matches [1, 2]
    counts = count_compare_rust(x, dat, "count.obs")
    np.testing.assert_array_equal(counts, [2, 1])

def test_mx_my_compare_rust():
    NA = np.int32(-2147483648)
    mat_x = np.array([[1, NA], [3, 4]], dtype=np.int32)
    mat_y = np.array([[1, 2], [3, 4]], dtype=np.int32)
    # Row 0 of mat_y: [1, 2]. 
    # Matches row 0 of mat_x: [1, NA] (since non-NA values match)
    # Row 1 of mat_y: [3, 4].
    # Matches row 1 of mat_x: [3, 4]
    matches = mx_my_compare_rust(mat_x, mat_y)
    # 1-based indexing
    assert matches == [[1], [2]]
