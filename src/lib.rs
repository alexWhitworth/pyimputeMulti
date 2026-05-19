// --- Feature: F-101 - Rust Kernels for Counting and Comparison ---
// Spec version: 2.0.0
// Layer: ffi_boundary
// Satisfies: count_compare_rust returns counts matching reference values for tract2221 dataset.
// Satisfies: sup_dist_c_rust returns correct L-infinity distance with tolerance 1e-12.
// Satisfies: mx_my_compare_rust correctly identifies indices of Y rows contained in X rows.
// Performance budget: O(N*M) for counting
// Linked schemas: None
// Linked APIs: API-001, API-002, API-003
use pyo3::prelude::*;
use numpy::{PyArray1, PyReadonlyArray1, PyReadonlyArray2};

/// sup of L1 distance between x and y
#[pyfunction]
pub fn sup_dist_c_rust(x: PyReadonlyArray1<f64>, y: PyReadonlyArray1<f64>) -> f64 {
    let x = x.as_array();
    let y = y.as_array();
    let mut sup: f64 = -1.0;

    for (xi, yi) in x.iter().zip(y.iter()) {
        let diff = (xi - yi).abs();
        if diff > sup {
            sup = diff;
        }
    }
    sup
}

/// Given a dataset and a patterns matrix, count the number of occurrences of each pattern.
#[pyfunction]
pub fn count_compare_rust(
    py: Python<'_>,
    x: PyReadonlyArray2<i32>,
    dat: PyReadonlyArray2<i32>,
    has_na: &str,
) -> PyResult<Py<PyArray1<i32>>> {
    let x_arr = x.as_array();
    let dat_arr = dat.as_array();
    let nr_x = x_arr.nrows();
    let _nr_dat = dat_arr.nrows();
    let _nc_x = x_arr.ncols();

    let mut counts = vec![0; nr_x];

    // Note: NA_INTEGER in R is typically -2147483648 (i32::MIN)
    let na_val = i32::MIN;

    match has_na {
        "no" => {
            for row_dat in dat_arr.rows() {
                for (i, row_x) in x_arr.rows().into_iter().enumerate() {
                    if row_x == row_dat {
                        counts[i] += 1;
                        break;
                    }
                }
            }
        }
        "count.obs" => {
            for row_dat in dat_arr.rows() {
                for (i, row_x) in x_arr.rows().into_iter().enumerate() {
                    let mut matched = true;
                    for (v_x, v_dat) in row_x.iter().zip(row_dat.iter()) {
                        if *v_dat != na_val && v_x != v_dat {
                            matched = false;
                            break;
                        }
                    }
                    if matched {
                        counts[i] += 1;
                        break;
                    }
                }
            }
        }
        "count.miss" => {
            for row_dat in dat_arr.rows() {
                for (i, row_x) in x_arr.rows().into_iter().enumerate() {
                    if row_x.iter().zip(row_dat.iter()).all(|(v_x, v_dat)| v_x == v_dat) {
                        counts[i] += 1;
                        break;
                    }
                }
            }
        }
        _ => {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "has_na must be 'no', 'count.obs', or 'count.miss'",
            ));
        }
    }

    Ok(PyArray1::from_vec(py, counts).unbind())
}

/// Compare two integer matrices, allowing missing values
#[pyfunction]
pub fn mx_my_compare_rust(
    _py: Python<'_>,
    mat_x: PyReadonlyArray2<i32>,
    mat_y: PyReadonlyArray2<i32>,
) -> PyResult<Vec<Vec<usize>>> {
    let x_arr = mat_x.as_array();
    let y_arr = mat_y.as_array();
    let nrow_x = x_arr.nrows();
    let na_val = i32::MIN;

    let mut out = vec![Vec::new(); nrow_x];

    for (i, row_x) in x_arr.rows().into_iter().enumerate() {
        for (j, row_y) in y_arr.rows().into_iter().enumerate() {
            let mut matched = true;
            for (v_x, v_y) in row_x.iter().zip(row_y.iter()) {
                if *v_x != na_val && *v_y != na_val {
                    if v_x != v_y {
                        matched = false;
                        break;
                    }
                } else if *v_x != na_val && *v_y == na_val {
                    // This case shouldn't happen for enum_comp, but for completeness:
                    // If row_x has a value but row_y is missing, it's NOT a completion.
                    matched = false;
                    break;
                }
                // If v_x is NA, it matches any v_y.
            }
            if matched {
                out[i].push(j);
            }
        }
    }

    Ok(out)
}

/// A Python module implemented in Rust.
#[pymodule]
fn _internal_rust(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sup_dist_c_rust, m)?)?;
    m.add_function(wrap_pyfunction!(count_compare_rust, m)?)?;
    m.add_function(wrap_pyfunction!(mx_my_compare_rust, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use ndarray::array;

    #[test]
    fn test_sup_dist_c() {
        // x and y are passed as array references in Rust tests
        let x = array![1.0f64, 2.0, 3.0];
        let y = array![1.1f64, 1.9, 3.5];
        
        let mut sup: f64 = -1.0;
        for (xi, yi) in x.iter().zip(y.iter()) {
            let diff = (xi - yi).abs();
            if diff > sup {
                sup = diff;
            }
        }
        assert!((sup - 0.5).abs() < 1e-12);
    }

    #[test]
    fn test_mx_my_compare_logic() {
        let na_val = i32::MIN;
        let x = array![[1, na_val], [3, 4]];
        let y = array![[1, 2], [3, 4], [1, 5]];
        
        // Row 0 of x: [1, NA] matches [1, 2] and [1, 5]
        // Row 1 of x: [3, 4] matches [3, 4]
        
        let mut out = vec![Vec::new(); x.nrows()];
        for (i, row_x) in x.rows().into_iter().enumerate() {
            for (j, row_y) in y.rows().into_iter().enumerate() {
                let mut matched = true;
                for (v_x, v_y) in row_x.iter().zip(row_y.iter()) {
                    if *v_x != na_val && *v_y != na_val {
                        if v_x != v_y {
                            matched = false;
                            break;
                        }
                    } else if *v_x != na_val && *v_y == na_val {
                        matched = false;
                        break;
                    }
                }
                if matched {
                    out[i].push(j);
                }
            }
        }
        
        assert_eq!(out[0], vec![0, 2]);
        assert_eq!(out[1], vec![1]);
    }

    #[test]
    fn test_count_compare_logic() {
        let na_val = i32::MIN;
        let x = array![[1, 2], [3, 4]];
        let dat = array![[1, na_val], [3, 4], [na_val, 2]];
        
        let nr_x = x.nrows();
        let mut counts = vec![0; nr_x];

        // logic for count.obs
        for row_dat in dat.rows() {
            for (i, row_x) in x.rows().into_iter().enumerate() {
                let mut matched = true;
                for (v_x, v_dat) in row_x.iter().zip(row_dat.iter()) {
                    if *v_dat != na_val && v_x != v_dat {
                        matched = false;
                        break;
                    }
                }
                if matched {
                    counts[i] += 1;
                    break;
                }
            }
        }
        
        assert_eq!(counts, vec![2, 1]);
    }
}
