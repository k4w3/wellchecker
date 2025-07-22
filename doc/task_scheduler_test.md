# WellChecker - タスクスケジューラ登録テスト手順

## 1. 前提条件
- `wellchecker_app_with_task.zip` を解凍。
- `wellchecker.exe` が生成されている（PyInstaller でビルド済み）。
- Windows 10 / 11 のユーザー権限がある（管理者権限は不要）。

## 2. タスクスケジューラ登録
1. **`install_task.bat` を右クリック →「管理者として実行」**  
   （ユーザー権限でも動作しますが、環境によっては UAC により権限が必要になることがあります。）

2. バッチが以下を実行します：  
   - `%APPDATA%\WellChecker` フォルダを作成  
   - `wellchecker.exe` をコピー  
   - **既存の「WellChecker」タスクを削除**（エラーは無視される）  
   - **「ログオン時に WellChecker.exe を起動するタスク」を登録**

3. 「[INFO] WellCheckerタスクスケジューラ登録完了」と表示されたら成功。

## 3. 動作確認
1. Windows の **「タスクスケジューラ」**を開く。
2. **「タスクスケジューラライブラリ」** > **「WellChecker」** タスクが登録されているか確認。
3. **「右クリック → 実行」** で WellChecker.exe が起動するかテスト。

## 4. 一日一回起動ロジック確認
- `main.py` 内に追加された `already_executed_today()` が、  
  `%APPDATA%\WellChecker\last_run_date.txt` に当日の日付を記録。  
  同日に再起動すると即終了する。

**テスト方法:**  
1. WellChecker.exe を2回連続で実行 → 2回目は「WellCheckerは本日すでに実行済みです。」と表示して終了する。

## 5. タスク削除
- 自動起動が不要になったら `uninstall_task.bat` を実行する。
- 「[INFO] WellCheckerタスク削除完了」と表示されたらOK。

## 6. 注意事項
- **PCをスリープ/再起動してログオンするたびにタスクが呼ばれますが、アプリ側で同日2回目以降は即終了します。**
- **`last_run_date.txt` を削除すると再度その日中でも起動します（テスト時に有効）。**
