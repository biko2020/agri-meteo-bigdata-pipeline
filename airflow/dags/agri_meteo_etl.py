from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="agri_meteo_etl",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    extract = BashOperator(
        task_id="extract_weather",
        bash_command="docker exec spark python3 /app/scripts/extract.py"
    )

    transform = BashOperator(
        task_id="transform_weather",
        bash_command="docker exec spark spark-submit /app/scripts/transform.py"
    )

    load = BashOperator(
        task_id="load_to_postgres",
        bash_command="docker exec spark python3 /app/scripts/load.py"
    )

    extract >> transform >> load
