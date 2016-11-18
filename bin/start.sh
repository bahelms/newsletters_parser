#!/bin/bash

until docker run -it --rm --link db:pg postgres:9.6.1 psql -U postgres -h pg -c "select 1" -d postgres
do 
  echo "Postgres not ready"
  sleep 1
done

python main.py
