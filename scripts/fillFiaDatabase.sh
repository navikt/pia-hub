#! /usr/bin/env bash

DB_DUMP=../lydia-api/scripts/db/lydia-api-container-db_localhost-2023_12_01_13_01_04-dump.sql
PGPASSWORD=test psql -h localhost -p 5432 -U postgres -f $DB_DUMP > /dev/null