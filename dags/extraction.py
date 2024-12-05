from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from datetime import datetime


with DAG(
    dag_id="extraction",
    start_date=datetime(2024, 12, 10),
    # schedule="0 0 * * *"
    schedule_interval=None,
) as dag:
    links = BashOperator(
        task_id="get_links_property",
        bash_command='python /opt/airflow/scr/etl/extraction/links.py'
    )

    property = BashOperator(
        task_id="get_property",
        bash_command='python /opt/airflow/scr/etl/extraction/property.py'
    )

    real_state = BashOperator(
        task_id="get_real_state",
        bash_command='python /opt/airflow/scr/etl/extraction/real_state.py'
    )

    start_treatment = TriggerDagRunOperator(
        task_id="start_treatment",
        trigger_dag_id="treatment",
        wait_for_completion=True,
        deferrable=True,
    )

    links >> property >> real_state
