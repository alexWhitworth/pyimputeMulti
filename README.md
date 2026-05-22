# imputemulti

A Python library for multivariate multinomial data imputation using Expectation-Maximization (EM) and Data Augmentation (DA) algorithms, with a high-performance Rust core.

## Features
- **Multivariate multinomial imputation**: Fill missing values in categorical datasets.
- **Algorithms**: 
    - Expectation-Maximization (EM) algorithm.
    - Data Augmentation (DA) algorithm.
- **Priors**: Conjugate priors (Dirichlet) and data-dependent priors.
- **Performance**: High-performance Rust implementation for core counting and comparison functions.
    - Benchmarking: 10x - 100x faster than the original R/C++ implementation

## Installation

- From Github: `pip install git+https://github.com/alexwhitworth/pyimputeMulti.git`
- From [PyPI](https://pypi.org/project/imputemulti): `pip install imputemulti`


## Usage
```python
from imputemulti import multinomial_impute, load_tract2221

# Load example data
df = load_tract2221()

# Perform imputation
em_result = multinomial_impute(df, method="EM", conj_prior="none")
da_result = multinomial_impute(df, method="DA", conj_prior="none")

# Access imputed data
em_imputed_df = em_result.data[1]
da_imputed_df = da_result.data[1]
```

## Detailed Examples

- See `docs/`
    - [Basic Usage](docs/basic_usage.py)
    - [Tutorial](docs/tutorial.md)
    - [Full Manual](docs/imputemulti_manual.md)


## References:
1. Schafer, Joseph L. Analysis of incomplete multivariate data. Chapter 7. CRC press, 1997.
2. Darnieder, William Francis. Bayesian methods for data-dependent priors. Diss. The Ohio State University, 2011.

## Citation

If you use `imputeMulti` in your work, please cite the following:

```bibtex
@Manual{imputemulti_py,
    title = {{imputeMulti}: Imputation Methods for Multivariate Multinomial Data},
    author = {Alex Whitworth},
    year = {2021},
    howpublished = {\url{https://github.com/alexwhitworth/imputeMulti}},
    note         = {R package version 0.8.3; migrated to Python in 2026. Accessed: <Month DD, YYYY>}
}
```