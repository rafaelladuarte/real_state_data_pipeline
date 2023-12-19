#!/bin/bash

# Dar permissão de execução ao script
chmod +x start_project.sh

# Adicionar o diretório ao PYTHONPATH
export PYTHONPATH=$PYTHONPATH:~./brazilian_ecommerce_data_modeling/project

# Iniciar os contêineres Docker em segundo plano
sudo docker-compose up -d

# Inicializar o banco de dados do Apache Airflow
docker exec -it airflow-webserver airflow db init

# Criar um usuário no Apache Airflow
docker exec -it airflow-webserver airflow users create --username username --password password --firstname Admin --lastname Admin --role Admin --email admin@email.com

# Sair do contêiner
exit
