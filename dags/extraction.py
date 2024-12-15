from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow import DAG

from datetime import datetime


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id="extraction",
    default_args=default_args,
    start_date=datetime(2024, 12, 10),
    # schedule="0 0 * * *"
    schedule_interval=None,
) as dag:
    links = DockerOperator(
        task_id="get_links_property",
        image="etl-scripts",
        api_version="auto",
        auto_remove=True,
        command="etl/extraction/links.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False
    )

    property = DockerOperator(
        task_id="get_property",
        image="etl-scripts",
        api_version="auto",
        auto_remove=True,
        command="etl/extraction/property.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False
    )

    real_state = DockerOperator(
        task_id="get_real_state",
        image="etl-scripts",
        api_version="auto",
        auto_remove=True,
        command="etl/extraction/real_state.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False
    )

    start_treatment = TriggerDagRunOperator(
        task_id="start_treatment",
        trigger_dag_id="treatment",
        wait_for_completion=True,
        deferrable=True,
    )

    links >> property >> real_state 
    # >> start_treatment
