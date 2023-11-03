FROM python:3.10.9-buster

WORKDIR /home/eugene

COPY requirements.txt .

RUN pip install -r requirements.txt