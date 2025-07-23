@echo off
chcp 65001 >nul
echo [INFO] WellChecker exe ビルド開始...

:: 仮想環境を有効化（必要に応じてパスを調整）
call .\venv\Scripts\activate

:: PyInstaller実行
REM pyinstaller --onefile --name wellchecker main.py
flet pack main.py --name wellchecker
REM flet pack main.py --name wellchecker --onedir

echo [INFO] ビルド完了
echo output_dir: dist\wellchecker.exe
pause
