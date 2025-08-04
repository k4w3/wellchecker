@echo off
chcp 65001 >nul
setlocal

set "HAS_ERROR=0"
echo [INFO] WellChecker アンインストール処理を開始します...

:: タスク削除
echo [INFO] タスクスケジューラから WellChecker タスクを削除中...
schtasks /delete /tn "WellChecker" /f >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] タスク削除完了
) else (
    echo [ERROR] タスクが存在しないか、削除に失敗しました。
    set HAS_ERROR=1
)

:: アプリ設定フォルダの削除
echo [INFO] 設定フォルダを削除中 (%APPDATA%\WellChecker)...
rd /s /q "%APPDATA%\WellChecker"
if exist "%APPDATA%\WellChecker" (
    echo [ERROR] 設定フォルダの削除に失敗しました。
    set HAS_ERROR=1
) else (
    echo [OK] 設定フォルダの削除完了
)

:: 結果メッセージ
echo.
if "%HAS_ERROR%"=="0" (
    echo [SUCCESS] アンインストール処理が正常に完了しました。
) else (
    echo [WARN] 一部の処理に失敗しました。管理者に連絡してください。
)

pause
endlocal
