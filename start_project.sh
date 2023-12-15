export PYTHONPATH=$PYTHONPATH:~./brazilian_ecommerce_data_modeling/project

sudo docker-compose up -d

docker exec -it airflow-webserver /bin/bash

airflow users create --username username --password password --firstname Admin --lastname Admin --role Admin --email admin@email.com

exit