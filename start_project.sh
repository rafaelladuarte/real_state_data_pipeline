#!/bin/bash
chmod +x start_project.sh
export PYTHONPATH=$PYTHONPATH:~./brazilian_ecommerce_data_modeling/project
sudo docker-compose up -d
