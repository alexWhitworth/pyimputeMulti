# imputemulti

A Python library for multivariate multinomial data imputation using Expectation-Maximization (EM) and Data Augmentation (DA) algorithms, with a high-performance Rust core.

## Features
- Multivariate multinomial imputation.
- Expectation-Maximization (EM) algorithm.
- Data Augmentation (DA) algorithm.
- Support for conjugate priors (Dirichlet).
- High-performance Rust implementation for core counting and distance functions.

## Installation

- From Github: `git clone ... && uv pip install .` 
- From PyPI: (coming soon)

## Usage
```python
from imputemulti import multinomial_impute, load_tract2221

# Load example data
df = load_tract2221()

# Perform imputation
result = multinomial_impute(df, method="EM", conj_prior="none")

# Access imputed data
imputed_df = result.data[1]
```


## References:
1. Schafer, Joseph L. Analysis of incomplete multivariate data. Chapter 7. CRC press, 1997.
2. Darnieder, William Francis. Bayesian methods for data-dependent priors. Diss. The Ohio State University, 2011.

## Citation

If you use `pyimputeMulti` in your work, please cite the following:

```bibtex
@Manual{imputemulti_py,
    title = {{imputeMulti}: Imputation Methods for Multivariate Multinomial Data},
    author = {Alex Whitworth},
    year = {2021},
    howpublished = {\url{https://github.com/alexwhitworth/imputeMulti}},
    note         = {R package version 0.8.3; migrated to Python in 2026. Accessed: <Month DD, YYYY>}
}
```