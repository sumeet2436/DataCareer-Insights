from sqlalchemy import create_engine

try:
    engine = create_engine(
        "postgresql+psycopg2://postgres:sumeet@localhost:5432/job_market"
    )

    with engine.connect() as conn:
        print("Database Connected Successfully!")

except Exception as e:
    print("Error:")
    print(e)