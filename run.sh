#!/usr/bin/env bash

echo "Starting flask server and smoke-test containers."
docker-compose build
docker-compose up --abort-on-container-exit
