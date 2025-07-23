@echo off
chcp 65001 >nul
echo [INFO] WellChecker exe ビルド開始...

:: 仮想環境を有効化（必要に応じてパスを調整）
call .\venv\Scripts\activate

:: PyInstaller実行
:: pyinstaller --onefile --name wellchecker main.py
flet pack main.py --name wellchecker
:: flet pack main.py --name wellchecker --onedir

:: distフォルダからshareフォルダにコピー
if not exist share mkdir share
copy /Y dist\wellchecker.exe share\wellchecker.exe

echo [INFO] ビルド完了
echo output_dir: dist\wellchecker.exe
pause
