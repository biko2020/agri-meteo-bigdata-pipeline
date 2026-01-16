from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("AgriMeteoETL").getOrCreate()

df = spark.read.csv("data/raw/weather.csv", header=True, inferSchema=True)

df_clean = df.dropna()

df_agg = df_clean.groupBy("date").agg(
    avg("temp_max").alias("avg_temp"),
    avg("precipitation").alias("avg_precipitation")
)

df_agg.write.mode("overwrite").parquet("data/processed/weather.parquet")
