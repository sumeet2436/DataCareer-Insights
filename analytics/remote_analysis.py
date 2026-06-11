import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:sumeet@localhost:5432/job_market"
)

query = """
SELECT remote_ratio,
       COUNT(*) AS total_jobs
FROM fact_salaries
GROUP BY remote_ratio
ORDER BY remote_ratio;
"""

df = pd.read_sql(query, engine)

print(df)

df.to_csv("data/remote_analysis.csv", index=False)

print("CSV Saved Successfully")