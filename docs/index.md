# imputemulti

A Python library for multivariate multinomial data imputation using Expectation-Maximization (EM) and Data Augmentation (DA) algorithms, with a high-performance Rust core.

## Features
- **Multivariate multinomial imputation**: Fill missing values in categorical datasets.
- **Algorithms**: Support for both EM and DA algorithms.
- **Priors**: Conjugate priors (Dirichlet) and data-dependent priors.
- **Performance**: High-performance Rust implementation for core counting and comparison functions.

## Contents
- [Tutorial](tutorial.md)
- [References](#references)

## Installation

```bash
pip install git+https://github.com/alexwhitworth/pyimputeMulti.git
```

## Quick Start
```python
from imputemulti import multinomial_impute, load_tract2221

# Load example data
df = load_tract2221()

# Perform imputation
em_result = multinomial_impute(df, method="EM", conj_prior="none")

# Access imputed data
imputed_df = em_result.data[1]
```

## References
1. Schafer, Joseph L. Analysis of incomplete multivariate data. Chapter 7. CRC press, 1997.
2. Darnieder, William Francis. Bayesian methods for data-dependent priors. Diss. The Ohio State University, 2011.
