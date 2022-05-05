#!/bin/sh

psql -d postgres -c "CREATE USER postgres WITH PASSWORD 'postgres';" 
psql -v ON_ERROR_STOP=1 -d postgres -c "CREATE DATABASE internship_portal OWNER 'postgres';"
exec "$@"