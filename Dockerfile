FROM python:3.9.7-bullseye
RUN apt-get update

RUN mkdir -p /applications/lunar_phases
WORKDIR /applications/lunar_phases

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt