""" Module. """
import os
import logging

from _menu_writer import MenuWriter
from _exceptions import MenuWriterException


class Converter:

    def __init__(self, datei_pfad):
        self.__table = MenuReaderPDF(datei_pfad).get_table()

    def convert(self):
        try:
            return MenuWriter(self.__table).create_xlsx()
        except:
            raise MenuWriterException


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    # Converter("test.pdf").convert()
