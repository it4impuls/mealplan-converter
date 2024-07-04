if n[! -d ".venv" ]; then
  python -m venv .venv
fi

.venv\Scripts\pip install -r requirements.txt

if n[! -f "*.pdf" ]; then
   read -p "bitte fügen Sie die PDF dateien in diesen Ordner ein und drücke dannach enter."
fi

.venv\Scripts\python main.py