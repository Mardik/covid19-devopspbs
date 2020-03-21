FROM python:3

ENV PYTHONUNBUFFERED 0

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app

ADD    requirements.txt    /app/
RUN    pip install --upgrade pip
RUN    pip install -r requirements.txt