#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")

PROJECTS=("fia-arbeidsgiver-frontend")
for project in ${PROJECTS[@]}; do
  cd "$HUB_DIR/$project"
  echo ""
  echo "----------- $project -------------"
  echo ""
  bun install --frozen-lockfile
  bun run build
  builddir=$(dirname `find .next/standalone -type f -name server.js -exec ls {} \; | grep -v node_modules`)
  cp -r $builddir/. .next/standalone
done