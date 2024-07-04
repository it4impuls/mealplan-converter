#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ ! -d ".git" ]; then
    echo downloading converter...
    git clone --no-checkout https://github.com/it4impuls/mealplan-converter.git tmp/
    mv tmp/.git .git
    git reset --hard HEAD
    rm -r tmp
  
fi

if [ ! -d ".venv" ]; then
    echo installing virtual environment...
    python3 -m venv $SCRIPT_DIR/.venv
    echo done!\n
fi

source $SCRIPT_DIR/.venv/bin/activate
echo updating dependencies...
pip3 install -r requirements.txt  > /dev/null
echo done!

while [ ! ls SCRIPT_DIR/*.pdf &>/dev/null ] ; do 
    read -s -n 1 -p "keine PDF's gefunden. Bitte fügen Sie die PDF dateien in diesen Ordner ein und drücke dannach enter."
done


python3 main.py