import datetime
import os
from pathlib import Path


def get_log_file():
    return Path(os.getenv("APPDATA")) / "WellChecker" / "last_run_date.txt"


def already_executed_today():
    log_file = get_log_file()
    today = datetime.date.today().strftime("%Y-%m-%d")
    if log_file.exists():
        last_run = log_file.read_text(encoding="utf-8").strip()
        if last_run == today:
            return True
    return False


def write_last_run_date():
    log_file = get_log_file()
    today = datetime.date.today().strftime("%Y-%m-%d")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.write_text(today, encoding="utf-8")
