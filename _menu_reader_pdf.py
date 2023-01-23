""" Was macht die Datei. """
import logging
import os

import camelot.io as camelot

from _file_type_exception import FileTypeException


# import xlsxwriter

class MenuReaderPDF:
    """
    Klasse zum einlesen einer PDF-Datei.
    Sie bekommt einen Pfad zu einer PDF-Datei und gibt einen table zurück
    """
    def __init__(self, pfadzurdatei):
        self.pfadzurdatei = self.__validate_input(pfadzurdatei)
        self.table = self.__openreader()

    def get_table(self):
        return self.table

    def __openreader(self):
        """
        Funktion zum entgegennehmen eines Dateipfades.
        Gibt einen Table zurück.
        """
        try:
            tmp_table = camelot.read_pdf(self.pfadzurdatei)
            return tmp_table[0].df
        except Exception:
            logging.error('Fehler unbekannt!')
            raise Exception

    def __validate_input(self, nichtvalidierterpfad):
        match nichtvalidierterpfad:
            case None:
                raise TypeError
            case str() as x:
                match x:
                    case x if not self.__check_file_type(x):
                        raise FileTypeException
                    case x if not os.path.exists(x):
                        raise FileNotFoundError
        return nichtvalidierterpfad

    def __check_file_type(self, dateipfad):
        dateiname = self.__get_filename(dateipfad)
        if self.__get_file_type(dateiname) == "pdf":
            return True
        else:
            return False

    def __get_filename(self, dateipfad):
        return os.path.basename(dateipfad)

    def __get_file_type(self, dateiname):
        return dateiname.split(".")[-1]


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    obj = MenuReaderPDF("/home/itloft/Downloads/KW 40.pdf")
