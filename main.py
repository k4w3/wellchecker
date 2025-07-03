import flet as ft
import os
from pathlib import Path
from config_handler import load_config, config_exists
from settings_form import settings_form
from wellchecker_form import wellchecker_form

CONFIG_PATH = Path(os.getenv("APPDATA")) / "WellChecker" / "config.ini"
CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

def main(page: ft.Page):
    page.title = "WellChecker - 今日の体調チェックアプリ"
    page.window_width = 420
    page.window_height = 360
    page.window_resizable = False

    # config.ini が存在しなければ設定画面に遷移
    if not config_exists(CONFIG_PATH):
        settings_view = settings_form(page, config_path=CONFIG_PATH, is_first_time=True)
        page.controls.append(settings_view)
    else:
        health_view = wellchecker_form(page, config_path=CONFIG_PATH)
        page.controls.append(health_view)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
