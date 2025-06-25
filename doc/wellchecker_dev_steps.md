# 🧭 開発の進め方：おすすめのステップ（WellChecker - 今日の体調チェックアプリ）

この仕様書を元に、アプリ開発を以下のステップで進めるとスムーズです。

---

## ✅ ① 環境構築とベースプロジェクトの作成

- Python仮想環境を作成
- 必要ライブラリのインストール

```bash
pip install flet
```

- `wellchecker_app/` ディレクトリと `.py` ファイルを空で用意（仕様書にある構成）

---

## ✅ ② config.ini の読み書き機能を実装

**ファイル：** `config_handler.py`

- `config.ini` が存在するかチェック
- 無ければ初期設定用の値を空で作成
- `get_config()` と `save_config()` 関数を用意

---

## ✅ ③ settings_form.py：初期設定UIの実装

**flet で設定フォーム画面を作成**

- 社員ID、名前、上長名、上長メールを入力
- 「保存」ボタンで `config_handler.save_config()` を呼ぶ
- 保存後に `wellchecker_form.py` を表示

---

## ✅ ④ wellchecker_form.py：体調申告画面の実装

- ラジオボタン or セレクトボックスで体調選択
- 「送信」ボタンで CSV保存・必要ならメール送信
- その日の申告が済んでいれば送信ボタン無効化

---

## ✅ ⑤ log_manager.py：ログ保存と古いログ削除

- ログファイルの命名＆保存
- 起動時に日付とファイル数をチェックして古いログ削除

---

## ✅ ⑥ mail_sender.py：メール送信処理

- SMTPを使ってメール送信（体調が△/✕の場合）
- テスト用にGmailなどのSMTPで試してみるのもあり（2段階認証注意）

---

## ✅ ⑦ report_viewer.py：管理者向けの集計ビュー

- fletの`DataTable`や`Column`で日別・社員別のCSVを表示
- フィルターや並び替えは後からでもOK

---

## ✅ ⑧ main.py の起動制御

- `config.ini` がない場合は設定画面へ
- あれば体調申告フォームへ遷移

---

## ✅ ⑨ PyInstaller で EXE を生成

- 実行形式の確認
- スタートアップバッチの生成・確認

---

## 🧰 開発用ライブラリリスト

```bash
pip install flet configparser
```

---

## 📂 最初にやるべきこと：具体的に

✅ `config_handler.py`  
✅ `settings_form.py`（fletの画面構築）

この2つが動けば、アプリの「起動～設定～保存」の流れが確認できます。
