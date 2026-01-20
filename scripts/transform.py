import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, when

# -------------------------------------------------
# Logging
# -------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting Agri Meteo Spark ETL")

# -------------------------------------------------
# Spark Session
# -------------------------------------------------
spark = SparkSession.builder \
    .appName("AgriMeteoETL") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# -------------------------------------------------
# Read raw data
# -------------------------------------------------
input_path = "/app/data/raw/weather.csv"
logging.info(f"Reading raw data from {input_path}")

df = spark.read.csv(input_path, header=True, inferSchema=True)
logging.info(f"Raw rows count: {df.count()}")

# -------------------------------------------------
# Cleaning
# -------------------------------------------------
df_clean = df.dropna()
logging.info(f"Clean rows count: {df_clean.count()}")

# -------------------------------------------------
# Aggregations
# -------------------------------------------------
df_agg = df_clean.groupBy("date").agg(
    avg("temp_max").alias("avg_temp"),
    avg("precipitation").alias("avg_precipitation")
)

# -------------------------------------------------
# KPI métier (risque climatique)
# -------------------------------------------------
df_kpi = df_agg.withColumn(
    "climate_risk",
    when(col("avg_precipitation") < 1, "HIGH")
    .when(col("avg_precipitation") < 5, "MEDIUM")
    .otherwise("LOW")
)

logging.info("KPI climate_risk computed")

# -------------------------------------------------
# Write Parquet (Data Lake)
# -------------------------------------------------
parquet_path = "/app/data/processed/weather"
df_kpi.write \
    .mode("overwrite") \
    .partitionBy("date") \
    .parquet(parquet_path)

logging.info(f"Parquet written to {parquet_path}")

# -------------------------------------------------
# Write to PostgreSQL (JDBC)
# -------------------------------------------------
jdbc_url = "jdbc:postgresql://postgres:5432/agri_db"

df_kpi.write \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "weather_kpi") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

logging.info("Data successfully loaded into PostgreSQL")

# -------------------------------------------------
spark.stop()
logging.info("Spark ETL finished successfully")
