import flet as ft
from datetime import datetime
import csv
import os
from pathlib import Path
from config_handler import load_config

def wellchecker_form(page: ft.Page, config_path: Path):
    page.title = "今日の体調申告"

    config = load_config(config_path)
    today = datetime.now().strftime("%Y-%m-%d")
    submitted = False
    status_text = ft.Text(value="", color=ft.Colors.GREEN, size=12)

    radio_group = ft.RadioGroup(
        content=ft.Column([
            ft.Text("今日の体調を選択してください", size=18),
            ft.Radio(value="◎", label="◎ 絶好調"),
            ft.Radio(value="○", label="○ 普通"),
            ft.Radio(value="△", label="△ 少し体調が悪い"),
            ft.Radio(value="✕", label="✕ 体調が悪い"),
        ])
    )

    def on_submit(e):
        nonlocal submitted
        if not radio_group.value:
            status_text.value = "体調を選択してください。"
            status_text.color = ft.Colors.RED
            page.update()
            return
        if submitted:
            status_text.value = "本日はすでに申告済みです。"
            status_text.color = ft.Colors.RED
            page.update()
            return

        record = [today, config['employee_id'], config['name'], radio_group.value]
        log_dir = os.path.join(os.getenv("APPDATA"), "WellChecker", "logs")
        os.makedirs(log_dir, exist_ok=True)
        file_path = os.path.join(log_dir, f"{today}_{config['employee_id']}.csv")

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["日付", "社員ID", "名前", "体調"])
            writer.writerow(record)

        # ✉️ メール送信は体調が △ or ✕ の場合に後で実装
        if radio_group.value in ["△", "✕"]:
            status_text.value = f"{radio_group.value} 申告完了（※上長に通知が必要です）"
        else:
            status_text.value = f"{radio_group.value} 申告完了しました。"

        submitted = True
        status_text.color = ft.Colors.GREEN
        page.update()

    return ft.Column([
        radio_group,
        ft.ElevatedButton("申告", on_click=on_submit),
        status_text
    ], tight=True, alignment=ft.MainAxisAlignment.START)
