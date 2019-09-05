#!/bin/bash

YELLOW='\033[1;33m'
NC='\033[0m'

TODAY=$(date "+%Y-%m-%d")

printf "${YELLOW}Creating build directory...${NC}\n"
cp -r src build

printf "${YELLOW}Installing requirements...${NC}\n"
mkdir -p /code/venv
python3.6 -m venv /code/venv/lambda
source /code/venv/lambda/bin/activate
pip install wheel
pip install -r requirements.txt

printf "${YELLOW}Creating archive...${NC}\n"
cd build
zip -r9 /code/build/lambda_${TODAY}.zip .
cd /code/venv/lambda/lib/python3.6/site-packages
zip -r9 /code/build/lambda_${TODAY}.zip .
cd /code/build
mv lambda_${TODAY}.zip ../
cd ../

printf "${YELLOW}Removing build artifacts...${NC}\n"
rm -rf build
rm -rf venv

printf "${YELLOW}Done${NC}\n"

