import datetime
from pathlib import Path

import flet as ft

from mail_sender import send_health_report
from settings_form import settings_form
from utils import write_last_run_datetime


def wellchecker_form(page: ft.Page, config_path: Path):

    page.title = "体調申告 - WellChecker"
    page.window_width = 420
    page.window_height = 460
    page.window_resizable = False

    today = datetime.date.today().strftime("%Y-%m-%d")
    submitted = False
    status = ft.Text(value="", size=12, color=ft.Colors.GREEN)
    selected_condition = ft.Ref[ft.Container]()

    comment_field = ft.TextField(
        label="コメント（任意）",
        width=380,
        height=70,
        multiline=True,
        max_lines=3,
        hint_text="例）少し頭痛があります。午前は軽めの作業にしたいです。",
    )

    def on_condition_select(e):
        for c in condition_options.controls:
            c.bgcolor = ft.Colors.GREY_200
        e.control.bgcolor = ft.Colors.BLUE_200
        selected_condition.current = e.control
        page.update()

    def on_submit(e):
        nonlocal submitted
        if not selected_condition.current:
            status.value = "体調を選択してください。"
            status.color = ft.Colors.RED
        elif submitted:
            status.value = "本日はすでに申告済みです。"
            status.color = ft.Colors.RED
        else:
            condition = selected_condition.current.data
            status.value = f"{today} の体調 ({condition}) を申告しました。"
            submitted = True
            status.color = ft.Colors.GREEN

            # メール送信処理（△または✕のときのみ）
            if condition in ["△", "✕"]:
                try:
                    send_health_report(
                        config_path=config_path,
                        condition=condition,
                        comment=(comment_field.value or "").strip() or None,
                    )
                except Exception as ex:
                    status.value += f"\n[メール送信失敗] {ex}"
                    status.color = ft.Colors.RED

            # 実行記録
            write_last_run_datetime()

        page.update()

    def build_condition_tile(emoji, label, data, description):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(emoji, size=80),
                    ft.Text(label, size=24),
                    ft.Text(description, size=12, color=ft.Colors.GREY_600),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.GREY_200,
            border_radius=10,
            padding=20,
            width=180,
            height=240,
            ink=True,
            data=data,
            on_click=on_condition_select,
        )

    def go_to_settings(e):
        page.controls.clear()
        page.controls.append(settings_form(page, config_path))
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("体調申告 - WellChecker"),
        center_title=True,
        bgcolor=ft.Colors.BLUE_300,
        actions=[ft.IconButton(icon=ft.Icons.SETTINGS, on_click=go_to_settings)],
    )

    condition_options = ft.Row(
        [
            build_condition_tile("😊", "◎", "◎", "元気いっぱい！"),
            build_condition_tile("🙂", "○", "○", "いつも通り"),
            build_condition_tile("😐", "△", "△", "少し不調"),
            build_condition_tile("😷", "✕", "✕", "休むかも..."),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    )

    submit_button = ft.ElevatedButton("体調を送信", on_click=on_submit, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
    return ft.Column(
        [
            ft.Row([ft.Text("今日の体調を申告してください", size=18, expand=True)]),
            ft.Divider(),
            condition_options,
            ft.Container(height=20),
            comment_field,
            ft.Container(height=10),
            submit_button,
            status,
        ],
        spacing=12,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
