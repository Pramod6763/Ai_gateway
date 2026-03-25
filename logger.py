import json
from datetime import datetime

LOG_FILE = "logs.json"

def log_request(prompt, model, reason, latency, cache):
    log_entry = {
        "time": str(datetime.now()),
        "prompt": prompt[:50],
        "model": model,
        "reason": reason,
        "latency": latency,
        "cache": cache
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)