# logger.py
# This module provides a function to log usage events to a JSONL file.

import os
import json
from datetime import datetime
from pathlib import Path

def log_usage_event(event_type, details):
    """
    Write a usage event to the daily JSONL log file under logs/usage/.
    
    Args:
        event_type (str): Type of event (e.g., "startup_check", "command_run", "task_action")
        details (dict): Additional data describing the event
    """
    log_dir = Path("logs/usage")
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / f"{datetime.now():%Y_%m_%d}_usage.jsonl"
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        **details
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")