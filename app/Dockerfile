FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /home/eugene

# System dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]
