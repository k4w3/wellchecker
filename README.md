# 今日の体調チェックアプリ

毎朝PC起動時にその日の体調を申告するためのデスクトップアプリです。  
申告された内容はCSVとして保存され、「△」「✕」などの体調不良時には自動で上長にメールが送信されます。

---

## 機能概要

- ◎ / ○ / △ / ✕ で体調を申告
- CSVファイルとしてローカル保存
- 「△」「✕」の場合は上長にメールで自動通知
- ログは日付別に保存され、一定期間・容量を超えると自動削除
- 初回起動時に設定画面表示（ユーザー情報・メール情報登録）

---

## 技術構成

| 項目 | 内容 |
|------|------|
| 言語 | Python 3.x |
| GUI | [Flet](https://flet.dev/) |
| パッケージ化 | PyInstaller |
| メール送信 | pywin32 (Outlook COM) |

---

## 初期設定時に必要な情報

- 社員ID・名前
- 上長の名前・メールアドレス
- 自分のメールアドレス（送信元）
- 自分のメールパスワード（またはアプリパスワード）

> Gmailを利用する場合、[アプリパスワードの設定](https://support.google.com/accounts/answer/185833)が必要です。

---

## 主なファイル構成

```
wellchecker_app/
├── main.py
├── settings_form.py
├── wellchecker_form.py
├── mail_sender.py
├── config_handler.py
├── log_manager.py
├── report_viewer.py
├── utils.py
├── assets/
│   └── icon.ico
├── logs/
└── config.ini
```

---

## 起動方法

ライブラリインストール：
   ```bash
   pip install -r requirements.txt
   ```
アプリ起動：
   ```bash
   python main.py
   ```

---

## メール通知

- 体調が「△」「✕」の場合、設定された上長に自動でメールを送信します。
- SMTP認証情報は初回設定時に登録してください。

---

## ログ保存先

- `%APPDATA%\WellChecker\logs\` 以下に日付＋社員IDのCSVが保存されます。
- ネットワーク共有先（`\\fileserver\wellchecker_reports\`）にも転送可能です（※未実装）。

---

## セキュリティ注意点

- メールパスワードは `.ini` ファイルに平文で保存されます。
- 社内運用時にはセキュリティ対策（暗号化や資格情報ストア利用）をご検討ください。

---

## 今後の拡張候補

- 未申告者リスト作成
- 管理画面からの集計表示（グラフなど）
- Excel出力
