#!/usr/bin/env bash

SCRIPTDIR=$(pwd)
PROJECTS=("fia-arbeidsgiver-frontend")
for project in ${PROJECTS[@]}; do
  cd "$SCRIPTDIR"
  cd "../$project"
  echo ""
  echo "----------- $project -------------"
  echo ""
  bun install --frozen-lockfile
  bun run build
  builddir=$(dirname `find .next/standalone -type f -name server.js -exec ls {} \; | grep -v node_modules`)
  cp -r $builddir/. .next/standalone
  rm -rf $builddir
done