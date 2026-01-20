from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "agri-data",
    "retries": 1,
}

with DAG(
    dag_id="agri_meteo_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    extract = BashOperator(
        task_id="extract_weather",
        bash_command="python3 /app/scripts/extract.py"
    )

    transform_load = BashOperator(
        task_id="spark_transform_load",
        bash_command="/opt/spark/bin/spark-submit /app/scripts/transform.py"
    )

    extract >> transform_load
