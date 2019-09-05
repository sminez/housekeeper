FROM ubuntu:bionic

RUN apt-get update -y --fix-missing
RUN apt-get install -y build-essential
RUN apt-get install -y software-properties-common
RUN apt-get install -y zip
RUN apt-get install -y python3  # python3.6 on bionic
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-venv

#create code mount
ADD . /code
WORKDIR /code
