from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.bash import BashOperator
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
    'dag_migracao_postgres',
    default_args={
        'start_date': datetime(2024, 12, 1),
        'retries': 1,
    },
    schedule_interval=None,
    catchup=False,
) as dag:

    tratar_dados_task = BashOperator(
        task_id='tratar_dados',
        bash_command=''
    )

    criar_tabelas = SQLExecuteQueryOperator(
        task_id='criar_tabelas',
        postgres_conn_id='postgres_default',
        sql='/opt/airflow/scr/etl/modeling/create_tables_oficial.sql',
    )

    inserir_dados = SQLExecuteQueryOperator(
        task_id='inserir_dados',
        postgres_conn_id='postgres_default',
        sql='/opt/airflow/scr/etl/modeling/insert_tables_oficial.sql',
    )

    tratar_dados_task >> criar_tabelas >> inserir_dados
