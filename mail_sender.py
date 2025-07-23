import os
import pythoncom
import win32com.client as win32
import logging
from pathlib import Path
from config_handler import load_config

# --- ログ設定 (ERROR以上のみログに残す) ---
log_dir = Path(os.getenv("APPDATA")) / "WellChecker"
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "wellchecker_error.log"

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename=str(log_file),
    filemode="a"
)

def send_health_report(config_path: Path, condition: str):
    pythoncom.CoInitialize()
    try:
        config = load_config(config_path)
        receiver_email = config.get("manager_email", "")
        cc_email = config.get("cc_email", "")
        employee_id = config.get("employee_id", "")
        name = config.get("name", "")

        if not receiver_email:
            error_msg = "上長のメールアドレスが設定されていません。"
            logging.error(error_msg)
            raise ValueError(error_msg)

        try:
            outlook = win32.Dispatch('Outlook.Application')
            mail = outlook.CreateItem(0)
            mail.To = receiver_email
            if cc_email:
                mail.CC = ", ".join([x.strip() for x in cc_email.split(",")])
            mail.Subject = f"【体調報告】{name} ({employee_id}) さんの状態: {condition}"
            mail.Body = (
                f"{name}（社員ID: {employee_id}）より、"
                f"本日の体調申告がありました。\n\n"
                f"【体調】: {condition}\n\n"
                "WellCheckerより自動送信"
            )
            mail.Send()
        except Exception as e:
            logging.error("メール送信失敗: %s", e)
            raise
    finally:
        pythoncom.CoUninitialize()
