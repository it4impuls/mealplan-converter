""" Was macht die Datei. """
import os
import logging
import coloredlogs
import camelot
# import xlsxwriter


class MenuReaderPDF:
    """ Klasse zum einlesen einer PDF-Datei. """

    def __init__(self, pfadzurdatei):
        self.pfadzurdatei = pfadzurdatei
    
    def openreader(self):
        """ Funktion zum entgegennehmen eines Dateipfades. """
        try:
            if os.path.exists(self.pfadzurdatei): # eventuell in init
                tables = camelot.read_pdf(self.pfadzurdatei)
                logging.debug(tables[0].df)
            else:
                logging.error('Die Datei: %s existiert nicht!', self.pfadzurdatei)
                raise FileNotFoundError
        except Exception:
            logging.error('Fehler unbekannt!')
            raise Exception
        

if __name__ == "__main__":

    logger = logging.getLogger()
    coloredlogs.install(level='DEBUG')
    coloredlogs.install(level='DEBUG', logger=logger)
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
