# Tutorial: Getting Started with imputemulti

This tutorial demonstrates how to use `imputemulti` to impute missing values in multivariate multinomial datasets.

## 1. Loading the Dataset

`imputemulti` comes with a sample dataset, `tract2221`, which contains categorical data with missing values.

```python
from imputemulti import load_tract2221

df = load_tract2221()
print(df.head())
print(f"Missing values:\n{df.isna().sum()}")
```

## 2. Performing Imputation

You can use either the Expectation-Maximization (EM) or Data Augmentation (DA) algorithm.

### Expectation-Maximization (EM)

EM provides Maximum Likelihood Estimates (MLE) for the parameters.

```python
from imputemulti import multinomial_impute

em_result = multinomial_impute(df, method="EM", conj_prior="none")

print(f"EM iterations: {em_result.mle_iter}")
print(f"EM log-likelihood: {em_result.mle_log_lik}")

# The imputed data is available in result.data[1]
imputed_df_em = em_result.data[1]
```

### Data Augmentation (DA)

DA is a Bayesian approach that provides posterior draws.

```python
da_result = multinomial_impute(df, method="DA", conj_prior="none", burnin=100, post_draws=500)

print(f"DA log-likelihood: {da_result.mle_log_lik}")

imputed_df_da = da_result.data[1]
```

## 3. Using Priors

`imputemulti` supports various conjugate priors.

### Data-Dependent Prior

```python
result_prior = multinomial_impute(df, method="EM", conj_prior="data.dep")
print(f"Result with data-dependent prior: {result_prior.mle_cp}")
```

## 4. Advanced Statistics

You can also calculate observed-data sufficient statistics directly.

```python
from imputemulti import multinomial_stats

# Observed counts for complete cases
x_y = multinomial_stats(df, output="x_y")
print(x_y.head())
```
