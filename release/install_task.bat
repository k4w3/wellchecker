@echo off
setlocal

:: このバッチファイルがあるディレクトリに移動
cd /d "%~dp0"

:: exeの配置
set APPDIR=%APPDATA%\WellChecker
if not exist "%APPDIR%" mkdir "%APPDIR%"
copy /Y wellchecker.exe "%APPDIR%"

:: タスクの作成
set TASK_NAME=WellChecker
set XML_FILE=%~dp0wellchecker_task.xml
schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1
schtasks /create /tn "%TASK_NAME%" /xml "%XML_FILE%" /f

echo [INFO] WellCheckerタスクスケジューラ登録完了
pause
endlocal
