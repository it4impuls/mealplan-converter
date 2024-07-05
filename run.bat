@echo off
SET SCRIPT_DIR=%~dp0
SET TMP_DIR=tmp\
goto begin
goto :EOF

:i_python
  echo python not found, please install python 
  start "" https://apps.microsoft.com/detail/9pjpw5ldxlz5
  pause
  goto:EOF

:i_git
  echo git not found, please install git
  start "" https://gitforwindows.org/
  pause
  goto:EOF

:download
  echo downloading converter...
  git clone --no-checkout https://github.com/it4impuls/mealplan-converter.git %TMP_DIR%
  dir tmp /a
  xcopy /s /e %SCRIPT_DIR%tmp\.git\* .git\ >nul
  DEL /q /S "tmp" >nul
  git reset --hard HEAD
  

:venv
  echo installing virtual environment...
  python3 -m venv %SCRIPT_DIR%.venv
  %SCRIPT_DIR%.venv\Scripts\activate.bat
  echo done!

:find_pdf
    IF NOT exist "%SCRIPT_DIR%*.pdf"(
      set /P var="keine PDF's gefunden. Bitte fügen Sie die PDF dateien in diesen Ordner ein und drücke dannach enter."
      @REM goto find_pdf
	)

:begin

  python --version 2>NUL & IF ERRORLEVEL 1 goto i_python

  git --version 2>NUL & IF ERRORLEVEL 1 goto i_git

  git pull || call :download
  %SCRIPT_DIR%.venv\Scripts\activate.bat || call :venv
  
  echo updating dependencies...
  pip3 "install" "-r" "requirements.txt" 
  echo done!

  call :find_pdf
  python3 "main.py"