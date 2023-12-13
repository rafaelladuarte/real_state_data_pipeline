sudo docker rm -f $(docker ps -aq)
sudo docker rmi -f $(docker images -aq)
sudo docker volume rm $(docker volume ls -q)
sudo docker network rm $(docker network ls -q)


# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres
# psql -h 172.23.0.4 -U username -d postgres -p 5433
# sudo docker logs airflow-webserver