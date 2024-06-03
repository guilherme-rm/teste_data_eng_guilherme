#!/bin/bash


DB1="fonte"
DB2="alvo"
DB_USER="postgres"
DB_PASSWORD="password"

PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -h localhost -c "DROP DATABASE IF EXISTS $DB1;"
PGPASSWORD=$DB_PASSWORD psql -U $DB_USER -h localhost -c "DROP DATABASE IF EXISTS $DB2;"
