@echo off
SET SCRIPT_DIR=%~dp0

:begin

  python --version 2>NUL
  if not errorlevel 0 goto i_python

  git --version 2>NUL
  if not errorlevel 0 goto i_git

  if not exist .git\ goto download

  if not exist .venv\ (
    echo "installing" "virtual" "environment..."
    python3 -m venv %SCRIPT_DIR%.venv
    echo "done!n"
  )

  source "%SCRIPT_DIR%.venv\bin\activate"
  echo "updating" "dependencies..."
  pip3 "install" "-r" "requirements.txt" 
  echo "done!"

  goto loop
  python3 "main.py"





:i_python
  start "" https://apps.microsoft.com/detail/9pjpw5ldxlz5

:i_git
  start "" https://gitforwindows.org/
  goto :EOF

:download
  echo "downloading" "converter..."
  git clone --no-checkout https://github.com/it4impuls/mealplan-converter.git tmp/
  move tmp\.git .git
  git reset --hard HEAD
  DEL /S "tmp"

:loop
    IF NOT exist "%SCRIPT_DIR%*.pdf" (
        set /P var="keine PDF's gefunden. Bitte fügen Sie die PDF dateien in diesen Ordner ein und drücke dannach enter."
        )
        goto loop