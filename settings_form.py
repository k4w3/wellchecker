import flet as ft
from config_handler import save_config, load_config
from pathlib import Path

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

    employee_id = ft.TextField(label="社員ID", width=300, value=config["employee_id"])
    name = ft.TextField(label="名前", width=300, value=config["name"])
    manager_name = ft.TextField(label="上長の名前", width=300, value=config["manager_name"])
    manager_email = ft.TextField(label="上長のメールアドレス", width=300, value=config["manager_email"])
    user_email = ft.TextField(label="あなたのメールアドレス", width=300, value=config.get("user_email", ""))
    status_text = ft.Text(value="", color=ft.Colors.GREEN, size=12)

    def on_submit(e):
        if not all([employee_id.value, name.value, manager_name.value, manager_email.value, user_email.value]):
            status_text.value = "すべての項目を入力してください。"
            status_text.color = ft.Colors.RED
        else:
            save_config(
                config_path=config_path,
                employee_id=employee_id.value,
                name=name.value,
                manager_name=manager_name.value,
                manager_email=manager_email.value,
                user_email=user_email.value
            )
            page.controls.clear()
            page.controls.append(wellchecker_form(page, config_path))
        page.update()

    return ft.Column([
        ft.Text("初回設定を行ってください", size=20),
        employee_id,
        name,
        manager_name,
        manager_email,
        user_email,
        ft.ElevatedButton("保存", on_click=on_submit),
        status_text
    ], tight=True, alignment=ft.MainAxisAlignment.START)
