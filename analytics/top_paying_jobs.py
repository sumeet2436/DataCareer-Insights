import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:sumeet@localhost:5432/job_market"
)

query = """
SELECT job_title,
       ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM fact_salaries
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 10;
"""

df = pd.read_sql(query, engine)

print(df)

df.to_csv("data/top_paying_jobs.csv", index=False)

print("CSV Saved Successfully")