"""
Basic usage example for the imputemulti package.
Demonstrates EM and DA imputation on the tract2221 dataset.
"""

from imputemulti import load_tract2221, multinomial_impute

def main():
    # 1. Load the dataset
    print("Loading tract2221 dataset...")
    df_full = load_tract2221()
    
    # (Full state space is very large)
    # Following the R manual, we will use a subset of columns for this example.
    cols = ['age', 'gender', 'marital_status', 'edu_attain', 'emp_status']
    df = df_full[cols].copy()
    
    print(f"Using subset of columns: {cols}")
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values per column:\n{df.isna().sum()}")

    # 2. EM Imputation
    print("\nRunning EM imputation...")
    em_res = multinomial_impute(df, method="EM", conj_prior="none")
    print(f"EM converged in {em_res.mle_iter} iterations.")
    print(f"EM Log-Likelihood: {em_res.mle_log_lik:.4f}")
    
    imputed_em = em_res.data[1]
    print(f"Missing values after EM: {imputed_em.isna().sum().sum()}")

    # 3. DA Imputation
    print("\nRunning DA imputation...")
    da_res = multinomial_impute(df, method="DA", conj_prior="none", burnin=100, post_draws=500)
    print(f"DA Log-Likelihood: {da_res.mle_log_lik:.4f}")
    
    imputed_da = da_res.data[1]
    print(f"Missing values after DA: {imputed_da.isna().sum().sum()}")

    print("\nBasic usage example completed successfully.")

if __name__ == "__main__":
    main()
