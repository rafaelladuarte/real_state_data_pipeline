FROM apache/airflow:2.7.0

USER root

RUN apt-get update && apt-get install -y \
    python3.9-minimal python3-pip build-essential \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow

RUN python -m pip install --upgrade pip

COPY requirements.txt /opt/airflow/
RUN pip install -r /opt/airflow/requirements.txt

ENV PYTHONPATH="/opt/airflow:$PYTHONPATH"

COPY dags/ /opt/airflow/dags/
COPY scr/ /opt/airflow/scr/

COPY .env /opt/airflow/.env
COPY client_secrets.json /opt/airflow/client_secrets.json 

USER root

RUN chown -R 1000:1000 /opt/airflow/dags /opt/airflow/scr
RUN chown -R 1000:1000 /opt/airflow/client_secrets.json /opt/airflow/.env

USER airflow
