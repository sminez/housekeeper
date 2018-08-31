#!/bin/bash

if [ $# -ne 1 ]
  then
    echo "You must supply a project name"
    exit
fi

PROJECT="$1"

if [ -d /code/target ]
  then
    rm -rf /code/target
fi
mkdir -p /build
mkdir -p /code/target
cd /build

pip3 install virtualenv
virtualenv $PROJECT
source $PROJECT/bin/activate
pip install -r /code/$PROJECT/requirements.txt

#start bundling
cd /code/$PROJECT/src
zip -r9 /code/target/bundle.zip *
cd /code/$PROJECT/binaries
zip -r9 /code/target/bundle.zip *
cd $VIRTUAL_ENV/lib/python3.6/site-packages
zip -r9 /code/target/bundle.zip *

#copy this to a file we can use elsewhere
DATE=`date +%Y-%m-%d`
FILENAME="$PROJECT-$DATE.zip"
cp /code/target/bundle.zip /code/$FILENAME
echo "created .zip file $FILENAME"
