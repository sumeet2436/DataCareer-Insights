import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("data/cleaned_ds_salaries.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:sumeet@localhost:5432/job_market"
)

# Load data into PostgreSQL
df.to_sql(
    name="fact_salaries",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully!")
print(f"Rows Loaded: {len(df)}")