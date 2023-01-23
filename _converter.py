""" Module. """
import os
import logging
from tkinter import filedialog
from _menu_reader_pdf import MenuReaderPDF


class Converter:


    def __init__(self):
        self.__dateipfad = self.__open_file_input_dialog()
        self.__menureader = MenuReaderPDF(self.__dateipfad)
        self.__table = self.__menureader.get_table()
        self.__read_table()

    def __open_file_input_dialog(self):
        return filedialog.askopenfilename()

    def __read_table(self):
        print(self.__table)



if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    obj = Converter()
    # logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
