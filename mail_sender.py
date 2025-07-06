import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from pathlib import Path
from config_handler import load_config

def send_health_report(config_path: Path, condition: str):
    config = load_config(config_path)
    sender_email = config.get("user_email", "")
    receiver_email = config.get("manager_email", "")
    employee_id = config.get("employee_id", "")
    name = config.get("name", "")

    if not sender_email or not receiver_email:
        raise ValueError("送信元または送信先メールアドレスが設定されていません。")

    subject = f"【体調報告】{name} ({employee_id}) さんの状態: {condition}"
    body = f"{name} さんが本日の体調を「{condition}」と申告しました。"

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = formataddr((name, sender_email))
    msg["To"] = receiver_email

    # --- ① GmailのSMTPサーバーを使う場合（テスト用） ---
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = "your_app_password_here"  # Gmailのアプリパスワード

    # --- ② 社内SMTPサーバーを使う場合（実運用） ---
    # smtp_server = "mail.yourcompany.local"   # ← 社内SMTPサーバーのホスト名 or IP
    # smtp_port = 25                            # ← 認証なしの場合（通常は25か587）
    # password = None                           # ← 必要に応じて設定（認証なしならNone）

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # 認証不要のSMTPの場合はコメントアウトしてもOK
        if password:
            server.login(sender_email, password)  # 認証が必要な場合
        server.send_message(msg)
