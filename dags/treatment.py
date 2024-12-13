from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow import DAG

from datetime import datetime


with DAG(
    dag_id="treatment",
    start_date=datetime(2024, 1, 1),
    # schedule="0 0 * * *"
    schedule_interval=None,
) as dag:

    property = DockerOperator(
        task_id="treat_property",
        image="etl-scripts",
        api_version="auto",
        auto_remove=True,
        command="etl/treatment/property.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )

    real_state = DockerOperator(
        task_id="treat_real_state",
        image="etl-scripts",
        api_version="auto",
        auto_remove=True,
        command="etl/treatment/real_state.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )

    start_load = TriggerDagRunOperator(
        task_id="start_load",
        trigger_dag_id="load",
        wait_for_completion=True,
        deferrable=True,
    )

    property >> real_state >> start_load
