@echo off
setlocal

:: WellChecker.exe�̔z�u��
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

echo [INFO] WellChecker�^�X�N�X�P�W���[���o�^����
pause
endlocal
