#!/bin/bash

# Parar e remover os contêineres definidos no docker-compose
sudo docker-compose down

# Remover todos os contêineres em execução
sudo docker rm -f $(docker ps -aq)

# Remover todas as imagens do Docker
sudo docker rmi -f $(docker images -aq)

# Remover todos os volumes do Docker
sudo docker volume rm $(docker volume ls -q)

# Remover todas as redes do Docker
sudo docker network rm $(docker network ls -q)
