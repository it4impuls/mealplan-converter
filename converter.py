""" Module. """
import os
import logging
from tkinter import filedialog
from _menu_reader_pdf import MenuReaderPDF


class Converter:

    def __init__(self):
        self.pfadzurdatei = MenuReaderPDF(self.__open_file_input_dialog())

    def __open_file_input_dialog(self):
        return filedialog.askopenfilename()


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    convertor = Converter()
