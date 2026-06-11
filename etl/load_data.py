import pandas as pd

df = pd.read_csv("data/ds_salaries.csv")

print("Columns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)