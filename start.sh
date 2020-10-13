#!/bin/bash
app="docker.auth"
docker build -t ${app} .
docker run -it --rm -p 80:80 --name=${app} -v $PWD/app:/app ${app}
