#!/bin/bash
set -e

CONTAINERS=$(docker ps -q)

if [ -n "$CONTAINERS" ]; then
  docker stop $CONTAINERS
else
  echo "No running containers to stop"
fi
