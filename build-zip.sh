#!/bin/bash
# Build a deployment zip archive of the source for housekeeper

YELLOW='\033[1;33m'
NC='\033[0m'

TODAY=$(date "+%Y-%m-%d")

printf "${YELLOW}Creating build directory...${NC}\n"
cp -r src build
printf "${YELLOW}Installing requirements...${NC}\n"
source ~/venvs/housekeeper/bin/activate
pip install -r requirements.txt
# python3.6 -m pip install -r requirements.txt -t build
printf "${YELLOW}Creating archive...${NC}\n"
cd build
zip -r9 ~/Personal/housekeeper/build/housekeeper_${TODAY}.zip .
#start bundling
cd ~/venvs/housekeeper/lib/python3.6/site-packages
zip -r9 ~/Personal/housekeeper/build/housekeeper_${TODAY}.zip .
cd ~/Personal/housekeeper/build
mv housekeeper_${TODAY}.zip ../
cd ../
printf "${YELLOW}Removing build artifacts...${NC}\n"
rm -rf build
printf "${YELLOW}Done${NC}\n"
