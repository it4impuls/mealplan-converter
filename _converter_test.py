""" Module. """
import os
import logging
import unittest
from _menu_reader_pdf import MenuReaderPDF
from _file_type_exception import FileTypeException


class TestMenuConverter(unittest.TestCase):

    # def test_input_is_none(self):


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()