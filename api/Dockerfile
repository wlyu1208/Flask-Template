FROM python:3.9-slim-buster

WORKDIR /flaskapp

RUN apt-get update
RUN apt install libpq-dev build-essential wget -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV DOCKERIZE_VERSION v0.2.0  

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY . /flaskapp

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]