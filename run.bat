@echo off
SET SCRIPT_DIR=%~dp0

:i_python
  WinAppDeployCmd install python

:i_git
  open "https://gitforwindows.org/"

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

REM UNKNOWN: {"type":"While","clause":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"[","type":"Word"},"suffix":[{"text":"!","type":"Word"},{"text":"ls","type":"Word"},{"text":"SCRIPT_DIR/*.pdf","type":"Word"}],"async":true},{"type":"Command","name":{"text":"]","type":"Word"},"prefix":[{"type":"Redirect","op":{"text":">","type":"great"},"file":{"text":"/dev/null","type":"Word"}}]}]},"do":{"type":"CompoundList","commands":[{"type":"Command","name":{"text":"read","type":"Word"},"suffix":[{"text":"-s","type":"Word"},{"text":"-n","type":"Word"},{"text":"1","type":"Word"},{"text":"-p","type":"Word"},{"text":"keine PDF's gefunden. Bitte fügen Sie die PDF dateien in diesen Ordner ein und drücke dannach enter.","type":"Word"}]}]}}
python3 "main.py"