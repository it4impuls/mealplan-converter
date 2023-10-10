# meaplan-converter

Installation unter Ubuntu:

1.) git clone https://github.com/it4impuls/meaplan-converter

2.) cd meaplan-converter

3.) pip install virtualenv oder ggf. vorher sudo apt install python3.10-venv

4.) python -m venv .venv

5.) source .venv/bin/activate

6.) pip install -r requirements.txt


Verwendung:

1.) cd meaplan-converter

2.) source .venv/bin/activate

3.) Ersetzten Sie die Dateien die mit KW anfangen mit den aktuellen (KW steht für Kalender Woche)
    achten Sie darauf das die Dateien folgendes Muster im Namen haben -> KW 30.pdf.

    In der Regel müssten es 4 - 5 Dateinen sein die wir von der Hauswirtschaft bekommen.
    Nachdem die aktuell KW Dateien in das Project Verzeichnis kopiert wurden und die Beispiel Dateinen gelöscht wurden geht es mit Schritt 4 weiter.


4.) python main.py

5.) Nach ein Paar Sekunden ist jetzt in dem Verzeichnis eine Datei new_merged_menu.xlsx .
    Das ist die Datei die in Mealplan hochgeladen werden muss.

6.) Diese Datei muss unbedingt vor Upload noch etwas bearbeitet werden. Es dürfen keine Anführungszeichen " oder Back \ oder Frontslashes / in den Feldern sein.
    Und die Datum Spalte muss als Datum mit dem Format yyyy-mm-dd erkannt und bestätigt werden.

6.) Öffnen Sie jetzt einen Browser (Firefox oder Chrome) und rufen Sie http://mealplan.impulsreha.local:8000/hwi
    Username: admin_hwi
    Passwort: ***REMOVED***

7.) CLicken Sie rechts oben auf Upload und wählen Sie Menu.

8.) Clicken Sie auf durchsuchen und suchen Sie new_merged_menu.xlsx

9.) Clicken Sie auf submit

10.)    Der Vorgang und die Benutzung ist noch lange nicht perfekt. 
        Falls mealplan nicht funktioniert müssen in der Datenbank die hochgeladenen Einträge per Hand gelöscht werden 
        und die new_merged_menu.xlsx hat entweder ein Fehler im Datum oder irgendwo ein Sonderzeichen. () Rundeklammer funktionieren.




