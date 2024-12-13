from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from datetime import datetime


with DAG(
    dag_id="hello",
    start_date=datetime(2024, 1, 1),
    # schedule="0 0 * * *"
    schedule_interval=None,
) as dag:
    hello = BashOperator(
        task_id="hello_world",
        bash_command="echo hello world"
    )

    @task()
    def airflow():
        print("airflow")

    hello >> airflow()
