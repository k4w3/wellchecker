import os
import sys
from pathlib import Path

import flet as ft

from config_handler import config_exists
from settings_form import settings_form
from utils import already_executed_recently
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


# 実行チェック
if already_executed_recently():
    print("WellCheckerは本日すでに実行済みです。")
    sys.exit()

if __name__ == "__main__":
    ft.app(target=main)
