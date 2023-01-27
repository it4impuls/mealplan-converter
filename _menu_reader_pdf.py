"""
Dieser Teil des Converters soll einen Pfad zu einer PDF-Datei bekommen
und diese dann einlesen und eine Table zurück geben.
"""
import os
import logging
import camelot.io as camelot
from camelot import plot
from _allergenic import Allergenic
from _exceptions import TableException, TableConditionException, FileTypeException, AllergenicException, \
    TablePagesNullException


class MenuReaderPDF:
    """
    Klasse zum einlesen einer PDF-Datei.
    Sie bekommt einen Pfad zu einer PDF-Datei und gibt einen table zurück
    """

    def __init__(self, pfadzurdatei):
        self.__pfadzurdatei = self.__validate_path(pfadzurdatei)
        self.__table = self.__openreader()
        self.__allergenics = Allergenic(self.__table[0][3]).get_allgernics()

    def get_table(self):
        return self.__table

    def get_allergenics(self):
        return self.__allergenics

    def build_output(self):
        for c in self.__table.columns:
            if c != 0:
                dataset = dict()
                dataset.update({"datum": self.__table.iloc[0, c]})
                dataset.update({"vollkost": self.__table.iloc[1, c]})
                dataset.update({"vegetarisch": self.__table.iloc[2, c]})
                return self.__pre_build_output(dataset)

    def __pre_build_output(self, pre_table):
        output = dict()
        tmp_dataset = dict()
        for i in pre_table:
            match i:
                case "datum":
                    tmp_dataset.update({"datum": self.__build_date_string(pre_table[i])})
                case "vollkost":
                    tmp_dataset.update({"vollkost": self.__build_meal_string(pre_table[i])})
                case "vegetarisch":
                    tmp_dataset.update({"vegetarisch": self.__build_meal_string(pre_table[i])})
            if len(tmp_dataset) == 3:
                output.update(tmp_dataset)
                del tmp_dataset
        return output

    def __build_date_string(self, date_string):
        ds_list = date_string.split(",")
        return ds_list[1]

    def __build_meal_string(self, meal_string):
        meal_string = meal_string.replace('GV ', '').strip()
        ms_list = meal_string.split("\n")
        new_meal_string = ""
        for i in ms_list:
            tmp_new_allergenic_string = " | Allergene: "
            """i ist der String in dem das Essen steht"""
            i = i.strip()
            l_tmp = i.split(" ")
            """
            l_tmp sind die Teile des Strings in dem das Essen steht
            0 ist das Menü
            -1 sind die Allergene
            """
            a_tmp = list(map(self.__find_and_replace_allergenics, l_tmp[-1].split(",")))
            n_tmp = [i for i in a_tmp if i is not None]
            for x in n_tmp:
                tmp_new_allergenic_string += x + ", "
            l_tmp[-1] = tmp_new_allergenic_string
            for e in range(len(l_tmp)):
                new_meal_string += l_tmp[e] + " "
        return new_meal_string

    def __find_and_replace_allergenics(self, x):
        for i in self.__allergenics:
            if x == i:
                return self.__allergenics[i]

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
                raise Exception
            else:
                return self.__validate_table(tmp_table[0].df)
        except (TableException, Exception) as error:
            raise error

    def __validate_table(self, zutestendetabelle):
        match zutestendetabelle.shape:
            case x if x[0] < 3:
                raise AllergenicException
            case x if x[1] < 4 or x[1] > 5:
                raise TableConditionException
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
        # format='%(asctime)s %(levelname)s: %(message)s',
        format='%(message)s',
        level=logging.DEBUG
    )

    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    print(MenuReaderPDF("test.pdf").build_output())

