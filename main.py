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

if __name__ == "__main__":
    ft.app(target=main)
