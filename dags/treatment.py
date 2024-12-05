from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from datetime import datetime


with DAG(
    dag_id="treatment",
    start_date=datetime(2024, 1, 1),
    # schedule="0 0 * * *"
    schedule_interval=None,
) as dag:

    property = BashOperator(
        task_id="treat_property",
        bash_command='python /opt/airflow/scr/etl/treatment/property.py'
    )

    real_state = BashOperator(
        task_id="treat_real_state",
        bash_command='python /opt/airflow/scr/etl/treatment/real_state.py'
    )

    start_load = TriggerDagRunOperator(
        task_id="start_load",
        trigger_dag_id="load",
        wait_for_completion=True,
        deferrable=True,
    )

    property >> real_state >> start_load
