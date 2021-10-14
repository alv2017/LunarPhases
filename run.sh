#!/bin/bash
# This script is expected to run on Debian family OS only

IMAGE_NAME=lunar_phases
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Exit script if the system is not running Debian type OS
if [ ! -f /etc/debian_version ]; then
  echo -e "${RED}\nError: OS Type Error: Non Debian type OS detected. Debian type OS required to run this script.\n${NC}";
  exit 1
fi

if [ "$(docker images -q ${IMAGE_NAME} 2> /dev/null)" = "" ]; then
  echo "Building docker image."
  docker build . -t ${IMAGE_NAME};
fi

if [ ${?} -ne 0 ]; then
  echo -e "${RED}\nApplication image build failed. Exiting the program.\n${NC}";
  exit 1;
fi

docker run --rm -d -p 127.0.0.1:80:8000 ${IMAGE_NAME}
if [ ${?} -ne 0 ]; then
  echo -e "${RED}\nFailed to start the container image. Exiting the program.\n${NC}";
  exit 1;
fi

echo -e "${GREEN}\nThe Lunar Phase Application is ready to run on http://127.0.0.1\n${NC}"
