#!/bin/sh


# set up env

read -p "Please set your env name: " env_name

echo 'your env name :' $env_name


echo 'creating env....'

conda create --name $env_name python=2.7 &&


# install library 

echo 'start install env.... '

source activate $env_name &&  pip install slackbot flask flask_restful  sqlalchemy  jsonify 

echo 'all env library installed successfully ! '




# if want to delete env 
# conda remove --name your_env_name --all


