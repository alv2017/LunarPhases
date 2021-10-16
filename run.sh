#!/bin/bash
# This script is expected to run on Debian family OS only

IMAGE_NAME=lunar_phases
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Re-build application image and start application containers
docker-compose up --build -d

if [ ${?} -ne 0 ]; then
  echo -e "${RED}\nThere was an error when starting application containers.\n${NC}";
  # Stop containers if they are running
  docker-compose down
  # Exit the program
  exit 1;
fi

# Migrate initial data and restart application containers
if [ ! -f "_data/migrated" ]; then
    touch "_data/migrated";
    chmod 000 "_data/migrated";
    CNT=0;

    # Wait for Postgres service to start
    sleep 1;

    docker exec lunar_phases /bin/bash -c "python manage.py makemigrations";
    docker exec lunar_phases /bin/bash -c "python manage.py migrate";
    while [ "${?}" -ne 0 ]; do
      # If database service didn't start in approx. 10 seconds, then exit the program and tidy up
      if [ ${CNT} -eq 10 ]; then
        docker-compose down;
        rm -rf _data;
        echo -e "${RED}\nUnable to connect to Postgres database. Exiting the program.\n${NC}";
        exit 1;
      fi
      sleep 1;
      CNT=$((CNT+1));
      docker exec lunar_phases /bin/bash -c "python manage.py migrate";
    done
    docker exec lunar_phases /bin/bash -c "DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --no-input --email=admin@example.com";
    # Restart application containers
    docker-compose down;
    docker-compose up -d
fi

echo -e "${GREEN}\nThe Lunar Phase Application is ready: http://127.0.0.1\n${NC}"
