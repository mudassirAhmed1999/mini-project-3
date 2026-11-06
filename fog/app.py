import os
import logging

from fastapi import FastAPI

FOG_ID = os.getenv("FOG_ID","fog_unkown")
ZONE = os.getenv("ZONE","zone_unkown")

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)
app = FastAPI(title="IoT Fog Node")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting %s for %s", FOG_ID, ZONE)

@app.get("/health")
async def health_check():
    return{
        "status": "ok",
        "fog_id": FOG_ID,
        "zone": ZONE
    }

