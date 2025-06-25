import flet as ft
from config_handler import save_config

def settings_form(page: ft.Page):
    page.title = "初回設定 - 今日の体調チェックアプリ"

    employee_id = ft.TextField(label="社員ID", width=300)
    name = ft.TextField(label="名前", width=300)
    manager_name = ft.TextField(label="上長の名前", width=300)
    manager_email = ft.TextField(label="上長のメールアドレス", width=300)
    status_text = ft.Text(value="", color=ft.Colors.GREEN, size=12)

    def on_submit(e):
        if not all([employee_id.value, name.value, manager_name.value, manager_email.value]):
            status_text.value = "すべての項目を入力してください。"
            status_text.color = ft.Colors.RED
            page.update()
            return

        save_config(
            employee_id=employee_id.value,
            name=name.value,
            manager_name=manager_name.value,
            manager_email=manager_email.value
        )
        status_text.value = "設定を保存しました。アプリを再起動してください。"
        status_text.color = ft.Colors.GREEN
        page.update()

    return ft.Column([
        ft.Text("初回設定を行ってください", size=20),
        employee_id,
        name,
        manager_name,
        manager_email,
        ft.ElevatedButton("保存", on_click=on_submit),
        status_text
    ], tight=True, alignment=ft.MainAxisAlignment.START)
