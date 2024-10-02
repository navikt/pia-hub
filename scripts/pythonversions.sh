#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")
FOLDERS=("ia-datafortelling" "fia-datafortelling")

for folder in ${FOLDERS[@]}; do
  DOCKERFILE="$HUB_DIR/$folder/Dockerfile"
  if [ -f "$DOCKERFILE" ]; then
    echo "$folder:"
    VERSIONS=$(grep -i "FROM python" "$DOCKERFILE" | sed -E 's/FROM python:([0-9]+\.[0-9]+(-slim)?).*/\1/' | sort -u)
    for version in $VERSIONS; do
      echo "  Python $version"
    done
  else
    echo "$folder: Dockerfile not found"
  fi
done