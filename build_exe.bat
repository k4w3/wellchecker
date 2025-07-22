@echo off
chcp 65001 >nul
echo [INFO] WellChecker exe ビルド開始...

:: 仮想環境を有効化（必要に応じてパスを調整）
call .venv\Scripts\activate

:: PyInstaller実行
pyinstaller --onefile --name wellchecker main.py

echo [INFO] ビルド完了
echo 出力先: dist\wellchecker.exe
pause
