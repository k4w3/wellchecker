@echo off
setlocal

:: ���̃o�b�`�t�@�C��������f�B���N�g���Ɉړ�
cd /d "%~dp0"

:: exe�̔z�u
set APPDIR=%APPDATA%\WellChecker
if not exist "%APPDIR%" mkdir "%APPDIR%"
copy /Y wellchecker.exe "%APPDIR%"

:: �^�X�N�̍쐬
set TASK_NAME=WellChecker
set XML_FILE=%~dp0wellchecker_task.xml
schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1
schtasks /create /tn "%TASK_NAME%" /xml "%XML_FILE%" /f

echo [INFO] WellChecker�^�X�N�X�P�W���[���o�^����
pause
endlocal
