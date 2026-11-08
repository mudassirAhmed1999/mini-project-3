import json
import os
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

LOG_DIR = Path(os.getenv("LOG_DIR", "/logs"))
LOG_FILE = LOG_DIR / "events.jsonl"

app = FastAPI(title="IoTs Logging and Monitoring")


class LogEvent(BaseModel):
    source: str = Field(min_length=1)
    event: str = Field(min_length=1)
    details: dict = Field(default_factory=dict)
    timestamp: str | None = None


@app.on_event("startup")
async def startup_event():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE.touch(exist_ok=True)


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "monitoring"}


@app.post("/logs", status_code=202)
async def receive_log(event: LogEvent):
    record = event.model_dump()
    record["received_at"] = datetime.now(timezone.utc).isoformat()
    try:
        with LOG_FILE.open("a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:
        raise HTTPException(status_code=500, detail="Could not persist log event") from exc
    return {"status": "accepted"}


@app.get("/logs/recent")
async def recent_logs(limit: int = 100):
    if limit < 1 or limit > 1000:
        raise HTTPException(status_code=400, detail="limit must be between 1 and 1000")
    if not LOG_FILE.exists():
        return {"events": []}
    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()[-limit:]
    return {"events": [json.loads(line) for line in lines]}
