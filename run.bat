@echo off
SET SCRIPT_DIR=%~dp0
SET TMP_DIR=tmp\
SET VENV_PATH=.venv\Scripts\activate
goto begin
goto :EOF

:find_pdf
  echo finding pdf's
    IF exist *.pdf (
      echo running Program...
      python "main.py" 
      echo done
      ) else (
      echo "no pdf found"
      set /P var="keine PDF's gefunden. Bitte fügen Sie die PDF dateien in diesen Ordner ein und drücke dannach enter."
      goto:EOF )
  goto:EOF

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


:begin
  @REM %SCRIPT_DIR%.venv\Scripts\activate.bat
  python --version 2>NUL & IF ERRORLEVEL 1 goto i_python

  git --version 2>NUL & IF ERRORLEVEL 1 goto i_git

  gswin32c.exe -v  >nul 2>&1|| gswin64c.exe -v  >nul 2>&1 || start "" https://ghostscript.com/releases/gsdnld.html

  git pull & IF ERRORLEVEL 128 call :download

  call %VENV_PATH% || call :venv

  echo updating dependencies...
  pip "install" "-r" "requirements.txt" >nul
  echo done!

  call :find_pdf
  