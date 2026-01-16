import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="agri_db",
    user="postgres",
    password="postgres"
)

df = pd.read_parquet("data/processed/weather.parquet")

df.to_sql("weather_kpi", conn, if_exists="replace", index=False)
conn.close()