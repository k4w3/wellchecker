import flet as ft
import os
from pathlib import Path
from config_handler import config_exists
from settings_form import settings_form
from wellchecker_form import wellchecker_form

CONFIG_PATH = Path(os.getenv("APPDATA")) / "WellChecker" / "config.ini"
CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

def main(page: ft.Page):
    page.controls.clear()
    if not config_exists(CONFIG_PATH):
        page.controls.append(settings_form(page, config_path=CONFIG_PATH))
    else:
        page.controls.append(wellchecker_form(page, config_path=CONFIG_PATH))
    page.update()


import datetime
from pathlib import Path

def already_executed_today():
    log_file = Path(os.getenv("APPDATA")) / "WellChecker" / "last_run_date.txt"
    today = datetime.date.today().strftime("%Y-%m-%d")
    if log_file.exists():
        last_run = log_file.read_text(encoding="utf-8").strip()
        if last_run == today:
            return True
    log_file.write_text(today, encoding="utf-8")
    return False

# 実行チェック
if already_executed_today():
    print("WellCheckerは本日すでに実行済みです。")
    exit()

if __name__ == "__main__":
    ft.app(target=main)
