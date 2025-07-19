import pandas as pd

df = pd.read_csv('data/consolidated_costs.csv')
summary = df.groupby('Category')[['Internal_Cost', 'Vendor_Cost']].mean().reset_index()
summary.to_excel('reports/cost_insights.xlsx', index=False)
print("Report generated.")
