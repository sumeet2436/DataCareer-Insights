import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:sumeet@localhost:5432/job_market"
)

query = """
SELECT experience_level,
       ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM fact_salaries
GROUP BY experience_level
ORDER BY avg_salary DESC;
"""

df = pd.read_sql(query, engine)

print(df)

df.to_csv("data/salary_by_experience.csv", index=False)

print("CSV Saved Successfully")