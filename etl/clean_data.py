import pandas as pd

df = pd.read_csv("data/ds_salaries.csv")

# Remove unwanted column
df.drop(columns=["Unnamed: 0"], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Check missing values
print(df.isnull().sum())

# Save cleaned data
df.to_csv("data/cleaned_ds_salaries.csv", index=False)

print("Data Cleaned Successfully")
print(df.shape)