""" Was macht die Datei. """
import os
import logging
import camelot


# import xlsxwriter

class MenuReaderPDF:
    """ Klasse zum einlesen einer PDF-Datei. """

    def __init__(self, pfadzurdatei):
        self.pfadzurdatei = pfadzurdatei

    def openreader(self):
        """ Funktion zum entgegennehmen eines Dateipfades. """
        self.validate_input()
        try:
            tables = camelot.read_pdf(self.pfadzurdatei)
            logging.debug(tables[0].df)
        except Exception:
            logging.error('Fehler unbekannt!')
            raise Exception

    def validate_input(self):
        match self.pfadzurdatei:
            case None:
                raise TypeError
            case str() as x:
                if not os.path.exists(x):
                    raise FileNotFoundError


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
