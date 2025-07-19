import pandas as pd

df_internal = pd.read_csv('data/sample_cost_data.csv')
df_vendor = pd.read_csv('data/external_vendor_rates.csv')

df_merged = pd.merge(df_internal, df_vendor, on='Service_ID', how='left')
df_merged.to_csv('data/consolidated_costs.csv', index=False)
print("Consolidated data saved.")
