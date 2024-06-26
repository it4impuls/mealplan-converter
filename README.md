# meaplan-converter

Diese App Liest die Monatlichen Menüs von der HWS und konvertiert diese zu excel, damit diese hochgeladen werden können.

## Voraussetzungen
* [Python](https://www.python.org/downloads/) (Stelle sicher der hakenbei "Add Python to environment variable" ist gesetzt)
* [git](https://github.com/git-guides/install-git)
* (Windows) [Ghostscript](https://ghostscript.com/releases/gsdnld.html)

## Installation und Verwendung


### Linux installation
1.) `git clone https://github.com/it4impuls/mealplan-converter`

2.) `cd mealplan-converter`

4.) `python -m venv .venv`

6.) `pip install -r requirements.txt`


### Windows installation
1.) `git clone https://github.com/it4impuls/meaplan-converter`

2.) `cd meaplan-converter`

4.) `python -m venv .venv`
* falls venv noch nicht vorhanden, installiere viretualenv `.venv\Scripts\pip install virtualenv`

5.) `.venv\Scripts\pip install -r requirements.txt`


## Verwendung:

1.) Ersetzten Sie die PDF-Dateien die mit KW anfangen mit den aktuellen (KW steht für Kalender Woche)
    achten Sie darauf das die Dateien folgendes Muster im Namen haben -> KW 30.pdf.

In der Regel müssten es 4 - 5 Dateien sein die wir von der Hauswirtschaft bekommen.
Nachdem die aktuell KW Dateien in das Project Verzeichnis kopiert wurden und die Beispiel Dateinen gelöscht wurden geht es mit Schritt 4 weiter.


2.)  Linux: `.venv/Scripts/python main.py`  Windows: `.venv\Scripts\python main.py`

3.) Nach ein Paar Sekunden ist jetzt in dem Verzeichnis eine Datei new_merged_menu.xlsx .
    Das ist die Datei die in Mealplan hochgeladen werden muss.

## Menü Hochladen

6.) Öffnen Sie jetzt einen Browser (Firefox oder Chrome) und rufen Sie das [Adminpanel](http://mealplan.impulsreha.local:8000/hwi) auf </br>
    Für die Loginddaten fragen Sie die Fachanleitung

7.) CLicken Sie rechts oben auf Upload und wählen Sie Menu.

8.) Clicken Sie auf durchsuchen und suchen Sie new_merged_menu.xlsx

9.) Clicken Sie auf submit

10.) geben Sie den Monat ein und stellen Sie sicher, dass die Menüs an den gegebenen wochentagen verfügbar sind.




