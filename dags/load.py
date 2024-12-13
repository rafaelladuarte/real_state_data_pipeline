from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow import DAG

from datetime import datetime


def treatment_file_sql(file_path):
    with open(file_path, 'r') as file:
        sql = file.read()

    cmds_sql = [
        cmd.strip()
        for cmd in sql.split(';')
        if cmd.strip() and not cmd.startswith('--')
    ]

    sql_treat = '; '.join(cmds_sql) + ';'

    return sql_treat


with DAG(
    'load',
    default_args={
        'start_date': datetime(2024, 12, 1),
        'retries': 1,
    },
    schedule_interval=None,
    catchup=False,
) as dag:

    criar_tabelas = PostgresOperator(
        task_id='create_tables',
        postgres_conn_id='postgres_default',
        sql='/opt/airflow/scr/etl/modeling/create_tables_oficial.sql',
    )

    inserir_dados = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres_default',
        sql='/opt/airflow/scr/etl/modeling/insert_tables_oficial.sql',
    )

    criar_tabelas >> inserir_dados
