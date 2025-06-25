
# ✅ 【WellChecker - 今日の体調チェックアプリ】仕様書最新版

---

## 📊 1. 開発技術・配布方法

| 項目       | 内容                      |
| -------- | ----------------------- |
| 開発言語     | Python 3.x              |
| GUIライブラリ | `flet` (モダンなGUI)        |
| パッケージ化   | `PyInstaller` (実行ファイル化) |
| 配布形式     | スクリプト配布、自動コピーとスタートアップ登録 |
| ログ管理     | 起動時にローカルログを自動整理         |

---

## 🛠️ 2. Python技術構成

| ライブラリ                  | 用途        | 備考                     |
| ---------------------- | --------- | ---------------------- |
| `flet`                 | GUI作成     | クロスプラットフォーム対応のGUIライブラリ |
| `configparser`         | INI設定読み書き | 標準                     |
| `csv`, `os`, `pathlib` | ログ出力/整理   | 標準                     |
| `smtplib`, `email`     | メール送信     | SMTP/セキュアプロトコル対応       |
| `datetime`             | 日付処理      | 標準                     |

---

## 📁 3. ディレクトリ構成

```
wellchecker_app/
├── main.py                  # 起動エントリー
├── wellchecker_form.py           # 体調申告UI
├── settings_form.py         # 設定画面
├── config_handler.py        # INI読み書き
├── mail_sender.py           # メール送信
├── log_manager.py           # ログ管理
├── report_viewer.py         # 集計表示ビュー
├── utils.py                 # 補助関数
├── assets/
│   └── icon.ico             # アイコン
├── logs/                    # ローカルログ
└── config.ini               # 設定ファイル
```

---

## 📅 4. 主な機能

### 4.1 設定情報の登録

- `config.ini` が無い場合、**初回起動時に設定画面を自動表示**
- 登録項目:
  - 社員ID / 名前
  - 上長名 / メールアドレス

#### config.ini 例

```ini
[USER]
employee_id = 12345
name = 山田 太郎

[MANAGER]
name = 佐藤 課長
email = sato.kacho@example.co.jp

[LOG]
max_days = 90
max_files = 100
```

---

### 4.2 体調申告UI

- 体調選択: 「◎」、「○」、「△」、「✕」
- 1日一回だけ申告可
- 実行すると CSV 保存 + メール送信(必要な場合)

---

### 4.3 記録方式 (CSV)

| 項目    | 詳細                                 |
| ----- | ---------------------------------- |
| 形式    | `YYYY-MM-DD,社員ID,名前,体調`            |
| 例     | `2025-06-19,12345,山田 太郎,◎`         |
| ファイル名 | `2025-06-19_12345.csv`             |
| 保存先   | - `%APPDATA%\wellchecker\logs\` |

- `\\fileserver\wellchecker_reports\` (共有先)

---

### 4.4 メール送信

- 体調が 「△」 、「✕」 の場合のみ
- 対象: `config.ini` の上長メールアドレス
- SMTP (TLS/587)

例:

```
今日、社員番号12345 (山田 太郎)より体調不良 (✕) の申告がありました。
上長: 佐藤 課長
```

---

### 4.5 ログ自動整理

| 条件   | 内容                                                  |
| ---- | --------------------------------------------------- |
| 実行時段 | 起動時                                                 |
| 整理条件 | - `max_days` 以上の日つきログを削除- `max_files` を超える場合、古い順に削除 |
| 設定元  | `config.ini` の `[LOG]` セクション                        |

---

### 4.6 管理者向け: 集計ビュー

| 項目   | 内容                               |
| ---- | -------------------------------- |
| 関数   | 社員別、日付別の体調申告状況を一覧表示              |
| 表示   | テーブル形式 (flet の DataTable/Column) |
| 準備   | `report_viewer.py`               |
| 元データ | logs/配下の CSV を解析                 |

---

## 🚀 5. 配布方法

### install.bat (Windows インストール)

```bat
@echo off
set APPDIR=%APPDATA%\wellchecker

mkdir "%APPDIR%"
copy /Y wellchecker.exe "%APPDIR%"
copy /Y config.ini "%APPDIR%" >nul 2>&1

:: スタートアップ登録
echo start "" "%APPDIR%\wellchecker.exe" > "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\start_wellchecker.bat"
```

---

## 📦 6. PyInstaller パッケージング

```bash
pyinstaller --onefile --noconsole --icon=assets/icon.ico main.py
```

---

## 🔄 7. 拡張案 (任意)

| 機能         | 内容                 |
| ---------- | ------------------ |
| ZIP化       | 旧ログを zip に封定       |
| 忘れもれチェック   | 未申告者を表示/通知         |
| Excel集計シート | CSV を統合した読み込みシート作成 |
