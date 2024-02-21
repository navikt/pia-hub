#!/usr/bin/env bash

SCRIPTDIR=$(pwd)
PROJECTS=("lydia-api" "fia-arbeidsgiver")
for project in ${PROJECTS[@]}; do
  cd "$SCRIPTDIR"
  cd "../$project"
  echo ""
  echo "----------- $project -------------"
  echo ""
  ./gradlew clean shadowJar -x test
done