#!/bin/bash
set -e

IMAGE="darshanbs2005/python-flask-app"
CONTAINER_NAME="flask-app"

# Stop and remove old container (if exists)
docker rm -f $CONTAINER_NAME || true

# Pull latest image
docker pull $IMAGE

# Run new container
docker run -d \
  --name $CONTAINER_NAME \
  -p 5000:5000 \
  --restart always \
  $IMAGE
