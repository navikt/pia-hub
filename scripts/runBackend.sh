#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")

cd $HUB_DIR

# -- Rydd opp gamle containere og slett databasen.
# TODO: Bør legges inn i flag på sikt.
docker-compose down -v

# -- Kjør opp fia-database, verifiser at den har startet og fyll inn data fra dump
# -- TODO: Bør få inn retry
docker-compose up fia-database -d
sleep 2
if ! docker-compose ps fia-database | grep Up; then
   echo "-- Klarte ikke kjøre opp fia-database --"
   exit 1
fi
scripts/fillFiaDatabase.sh

# -- Start opp backends og fia(lydia-radgiver-frontend)-frackend
docker-compose up fia-backend -d
docker-compose up fia-frackend -d
docker-compose up fia-arbeidsgiver -d

echo "fia-backend bør straks være tilgjengelig på http://localhost:8080/internal/isalive"
echo "fia-frackend bør straks være tilgjengelig på http://localhost:3000/internal/isalive"
echo "fia-arbeidsgiver bør straks være tilgjengelig på http://localhost:8081/internal/isalive"