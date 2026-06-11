import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:sumeet@localhost:5432/job_market"
)

query = """
SELECT company_size,
       COUNT(*) AS total_jobs
FROM fact_salaries
GROUP BY company_size
ORDER BY total_jobs DESC;
"""

df = pd.read_sql(query, engine)

print(df)

df.to_csv("data/company_size_analysis.csv", index=False)

print("CSV Saved Successfully")