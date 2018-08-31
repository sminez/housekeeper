FROM ubuntu:bionic
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

#get basic requirements
RUN apt-get update -y --fix-missing
RUN apt-get install -y build-essential
RUN apt-get install -y python3
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-setuptools
RUN apt-get update -y --fix-missing
RUN apt-get install -y python3-software-properties
RUN apt-get install -y git-core
RUN apt-get install -y zip
RUN apt-get install -y autoconf
RUN apt-get install -y libtool
RUN apt-get install -y wget

#grab and install python deps
RUN easy_install pip3

#create code mount
ADD . /code
WORKDIR /code
