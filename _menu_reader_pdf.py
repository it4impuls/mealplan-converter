"""
Dieser Teil des Converters soll einen Pfad zu einer PDF-Datei bekommen
und diese dann einlesen und eine Table zurück geben.
"""
import os
import logging
import camelot.io as camelot
from _exceptions import TableException, TableConditionException, FileTypeException


class MenuReaderPDF:
    """
    Klasse zum einlesen einer PDF-Datei.
    Sie bekommt einen Pfad zu einer PDF-Datei und gibt einen table zurück
    """
    def __init__(self, pfadzurdatei):
        self.__pfadzurdatei = self.__validate_path(pfadzurdatei)
        self.__table = self.__openreader()

    def get_table(self):
        return self.__table

    def __openreader(self):
        """
        Funktion zum entgegennehmen eines Dateipfades.
        Gibt einen Table zurück.
        Anmerkung: wenn die Datei kein Table enthält gibt es ein UserWarning den man auch
        abfangen könnte. Es gibt ein python Paket warnings welches diese Thema behandelt.
        """
        try:
            tmp_table = camelot.read_pdf(self.__pfadzurdatei)
            if tmp_table.n == 0:
                raise TableException
            else:
                return self.__validate_table(tmp_table[0].df)
        except (TableException, Exception) as error:
            raise error

    def __validate_table(self, zutestendetabelle):
        if zutestendetabelle.shape[0] != 4:
            raise TableConditionException
        elif zutestendetabelle.shape[1] > 5 | zutestendetabelle.shape[1] < 1:
            raise TableConditionException
        else:
            return zutestendetabelle

    def __validate_path(self, nichtvalidierterpfad):
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
