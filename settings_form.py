import re
from pathlib import Path

import flet as ft

from config_handler import load_config, save_config


def settings_form(page: ft.Page, config_path: Path):
    from wellchecker_form import wellchecker_form

    page.title = "初回設定 - WellChecker"

    config = load_config(config_path)
    is_initial = not config.get("employee_id")

    def on_back_click(e):
        if not is_initial:
            page.controls.clear()
            page.controls.append(wellchecker_form(page, config_path))
            page.update()

    if not is_initial:
        page.appbar = ft.AppBar(
            title=ft.Text("設定"),
            center_title=True,
            bgcolor=ft.Colors.BLUE_300,
            leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=on_back_click),
        )
    else:
        page.appbar = None

    employee_id = ft.TextField(label="社員ID", width=300, value=config.get("employee_id", ""))
    user_last_name = ft.TextField(label="（あなた）姓", width=300, value=config.get("user_last_name", ""))
    user_first_name = ft.TextField(label="（あなた）名", width=300, value=config.get("user_first_name", ""))
    manager_last_name = ft.TextField(label="（上長）姓", width=300, value=config.get("manager_last_name", ""))
    manager_first_name = ft.TextField(label="（上長）名", width=300, value=config.get("manager_first_name", ""))
    user_name_row = ft.Row(
        [user_last_name, user_first_name],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )
    manager_name_row = ft.Row(
        [manager_last_name, manager_first_name],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )
    manager_email = ft.TextField(label="上長のメールアドレス", width=300, value=config.get("manager_email", ""))
    cc_email = ft.TextField(label="CCメールアドレス（カンマ区切り可）", width=300, value=config.get("cc_email", ""))
    status_text = ft.Text(value="", color=ft.Colors.GREEN, size=12)

    def is_valid_email(email: str) -> bool:
        # 簡易的なメール形式チェック
        return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

    def on_submit(e):
        required = [
            employee_id.value,
            user_last_name.value,
            user_first_name.value,
            manager_last_name.value,
            manager_first_name.value,
            manager_email.value,
        ]
        if not all(required):
            status_text.value = "必須項目が未入力です。"
            status_text.color = ft.Colors.RED
        elif not is_valid_email(manager_email.value):
            status_text.value = "上長のメールアドレスが不正です。"
            status_text.color = ft.Colors.RED
        elif cc_email.value and any(not is_valid_email(addr.strip()) for addr in cc_email.value.split(",")):
            status_text.value = "CCメールアドレスの形式が不正です。"
            status_text.color = ft.Colors.RED
        else:
            save_config(
                config_path=config_path,
                employee_id=employee_id.value,
                user_last_name=user_last_name.value,
                user_first_name=user_first_name.value,
                manager_last_name=manager_last_name.value,
                manager_first_name=manager_first_name.value,
                manager_email=manager_email.value,
                cc_email=cc_email.value,
            )
            page.controls.clear()
            page.controls.append(wellchecker_form(page, config_path))
        page.update()

    return ft.Column(
        [
            ft.Text("初回設定を行ってください", size=20),
            employee_id,
            user_name_row,
            manager_name_row,
            manager_email,
            cc_email,
            ft.ElevatedButton("保存", on_click=on_submit),
            status_text,
        ],
        tight=True,
        alignment=ft.MainAxisAlignment.START,
    )
