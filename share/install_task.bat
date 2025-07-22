@echo off
setlocal

:: WellChecker.exeの配置先
set APPDIR=%APPDATA%\WellChecker
set APP=%APPDIR%\wellchecker.exe

if not exist "%APPDIR%" mkdir "%APPDIR%"
copy /Y wellchecker.exe "%APPDIR%"

schtasks /delete /tn "WellChecker" /f >nul 2>&1

schtasks /create ^
  /tn "WellChecker" ^
  /tr "\"%APP%\"" ^
  /sc onlogon ^
  /rl LIMITED ^
  /f

echo [INFO] WellCheckerタスクスケジューラ登録完了
pause
endlocal
