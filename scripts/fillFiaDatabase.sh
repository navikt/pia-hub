#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
HUB_DIR=$( dirname "$SCRIPT_DIR")

DB_DUMP=$HUB_DIR/lydia-api/scripts/db/lydia-api-container-db_localhost-2023_12_01_13_01_04-dump.sql
PGPASSWORD=test psql -h localhost -p 5432 -U postgres -f $DB_DUMP > /dev/null