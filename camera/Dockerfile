FROM python:3.13-slim

# curl is used for the zone-isolation test (1.3) and the container healthcheck
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copies the camera application into the container
COPY client.py .

CMD ["python", "-u", "client.py"]