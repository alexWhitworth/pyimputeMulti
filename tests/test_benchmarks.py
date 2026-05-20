# --- Feature: F-401 — Testing, Benchmarking and Validation ---
# Spec version: 2.0.0
# Layer: ffi_boundary
# Satisfies: Performance benchmarks show Rust implementation is at least 1.5x faster than R/C++ for core kernels.
# Performance budget: none specified
# Linked schemas: N/A
# Linked APIs: API-001, API-002, API-003

import numpy as np
import pandas as pd
import pytest

from imputemulti._internal_rust import count_compare_rust, sup_dist_c_rust, mx_my_compare_rust

@pytest.fixture(scope="module")
def sample_data():
    """
    Fixture to generate sample data for benchmarking.
    Mimics characteristics of a dataset like 'tract2221'.
    """
    n_rows = 10000
    n_cols = 5
    n_levels = 5 # Number of unique categories per column
    
    # Generate data with some missing values
    data = np.random.randint(0, n_levels, size=(n_rows, n_cols), dtype=np.int32)
    
    # Introduce NaNs as -1 for Rust compatibility
    num_nan = n_rows // 10 # 10% missing
    nan_indices = np.random.choice(n_rows * n_cols, num_nan, replace=False)
    data.flat[nan_indices] = -1 
    
    # Create x and dat for count_compare_rust
    x_rows = 100
    x_cols = n_cols
    x = np.random.randint(0, n_levels, size=(x_rows, x_cols), dtype=np.int32)
    
    # has_na for count_compare_rust
    has_na_flag = "no" # Assuming no NA's in x for now for simpler benchmarking
    
    # For mx_my_compare_rust: generate mat_y (complete patterns)
    # A smaller set of unique complete patterns
    mat_y_rows = 500
    mat_y_cols = n_cols
    mat_y = np.unique(np.random.randint(0, n_levels, size=(mat_y_rows, mat_y_cols), dtype=np.int32), axis=0)
    
    # For sup_dist_c_rust
    vec_len = 100
    vec1 = np.random.rand(vec_len)
    vec2 = np.random.rand(vec_len)

    return {
        "data": data,
        "x_count": x,
        "has_na": has_na_flag,
        "mat_y": mat_y,
        "vec1": vec1,
        "vec2": vec2,
    }


def test_benchmark_count_compare_rust(benchmark, sample_data):
    """
    Benchmark for count_compare_rust function.
    """
    data = sample_data["data"]
    x = sample_data["x_count"]
    has_na = sample_data["has_na"]
    benchmark(count_compare_rust, x, data, has_na)


def test_benchmark_sup_dist_c_rust(benchmark, sample_data):
    """
    Benchmark for sup_dist_c_rust function.
    """
    vec1 = sample_data["vec1"]
    vec2 = sample_data["vec2"]
    benchmark(sup_dist_c_rust, vec1, vec2)


def test_benchmark_mx_my_compare_rust(benchmark, sample_data):
    """
    Benchmark for mx_my_compare_rust function.
    """
    mat_x = sample_data["data"] # Using data with NAs for mat_x
    mat_y = sample_data["mat_y"]
    benchmark(mx_my_compare_rust, mat_x, mat_y)

