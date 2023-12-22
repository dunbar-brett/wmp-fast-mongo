FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /server

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# COPY ./.env /server/.env

RUN pip install --upgrade pip
COPY ./requirements.txt /server/requirements.txt
RUN pip install -r /server/requirements.txt

COPY . .