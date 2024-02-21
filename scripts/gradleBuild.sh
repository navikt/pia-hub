#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")
PROJECTS=("lydia-api" "fia-arbeidsgiver")

for project in ${PROJECTS[@]}; do
  echo ""
  echo "----------- $project -------------"
  echo ""
   cd "$HUB_DIR/$project"
  ./gradlew clean shadowJar -x test
done