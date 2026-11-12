FROM python:3.13-slim

# iproute2 -> tc/netem for the WAN delay (1.5); curl + ping for connectivity tests
RUN apt-get update \
    && apt-get install -y --no-install-recommends iproute2 iputils-ping curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY cloud/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY common/logging_client.py .
COPY cloud/app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]