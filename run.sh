#!/bin/bash
# This script is expected to run on Debian family OS only

IMAGE_NAME=lunar_phases
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# if application image doesn't exist, then build it
if [ "$(docker images -q ${IMAGE_NAME} 2> /dev/null)" = "" ]; then
  echo "Building docker image."
  docker build . -t ${IMAGE_NAME};
fi

if [ ${?} -ne 0 ]; then
  echo -e "${RED}\nApplication image build failed. Exiting the program.\n${NC}";
  exit 1;
fi

# start application container
docker run --rm --name=lunar_phases_app -d -p 127.0.0.1:80:8000 ${IMAGE_NAME}
if [ ${?} -ne 0 ]; then
  echo -e "${RED}\nFailed to start the container image. Exiting the program.\n${NC}";
  exit 1;
fi

echo -e "${GREEN}\nThe Lunar Phase Application is ready to run on http://127.0.0.1\n${NC}"
