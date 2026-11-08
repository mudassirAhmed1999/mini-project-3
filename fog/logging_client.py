import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone

LOG_COLLECTOR_URL = os.getenv(
    "LOG_COLLECTOR_URL", "http://172.28.4.30:9000/logs"
)


def send_event(source: str, event: str, details: dict | None = None) -> None:
    payload = {
        "source": source,
        "event": event,
        "details": details or {},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    request = urllib.request.Request(
        LOG_COLLECTOR_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=2):
            pass
    except (urllib.error.URLError, TimeoutError, OSError):
        # Logging must not prevent the fog service from starting or responding.
        pass
