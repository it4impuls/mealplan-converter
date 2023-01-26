"""Hier stehen die Fehler die im Datei-Pfad und Typ spezifiziert werden."""
class FileTypeException(Exception):
    """Ein Fehler der beim falschen Datei-Typ ausgelöst werden soll."""
    def __init__(self, message="The file has not the correct type"):
        self.message = message
        super().__init__(self.message)

class TablePagesNullException(Exception):
    """Ein Fehler der ausgelöst werden soll wenn es keine Pages in der Tabelle gibt."""
    def __init__(self, message="Tablepages are Null"):
        self.message = message
        super().__init__(self.message)

class TableException(Exception):
    """Ein Fehler der ausgelöst werden soll wenn etwas mit der Tabelle nicht stimmt."""
    def __init__(self, message="Anything is wrong with the table!"):
        self.message = message
        super().__init__(self.message)

class TableConditionException(Exception):
    """Ein Fehler der ausgelöst werden soll wenn die Tabelle nicht bestimmte Kriterien erfüllt"""
    def __init__(self, message="The table have not the right condition!"):
        self.message = message
        super().__init__(self.message)

class MenuReaderException(Exception):
    """Ein Fehler der ausgelöst werden soll wenn ein Fehler im MenuReader auftritt"""
    def __init__(self, message="Anything is wrong with the reader"):
        self.message = message
        super().__init__(self.message)

class MenuWriterException(Exception):
    """Ein Fehler der ausgelöst werden soll wenn ein Fehler im MenuReader auftritt"""
    def __init__(self, message="Anything is wrong with the writer"):
        self.message = message
        super().__init__(self.message)

class AllergenicException(Exception):
    """Ein Fehler der ausgelöst werden soll wenn ein Fehler im Allergenic auftritt"""
    def __init__(self, message="Anything is wrong with Allergenic"):
        self.message = message
        super().__init__(self.message)