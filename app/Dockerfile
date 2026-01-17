FROM python:3.10.9-buster
WORKDIR /home/eugene
COPY . .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y sqlite3
ENTRYPOINT ["sh", "entrypoint.sh"]
