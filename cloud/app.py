import logging
import os

from fastapi import FastAPI
from logging_client import send_event

CLOUD_ID = os.getenv("CLOUD_ID", "cloud")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="IoT Cloud Node")


@app.on_event("startup")
async def startup_event():
    logger.info("Starting cloud service: %s", CLOUD_ID)
    send_event("cloud", "service_started", {"cloud_id": CLOUD_ID})


@app.get("/health")
async def health_check():
    result = {"status": "ok", "cloud_id": CLOUD_ID}
    return result
