FROM apache/airflow:2.7.0

USER airflow

COPY dags/ /opt/airflow/dags/

USER root

RUN chown -R 1000:1000 /opt/airflow/dags

USER airflow
