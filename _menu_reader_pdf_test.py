""" Module. """
import os
import logging
import unittest
from _menu_reader_pdf import MenuReaderPDF
from _file_type_exception import FileTypeException


class TestMenuReaderPDF(unittest.TestCase):

    def test_input_is_none(self):
        with self.assertRaises(TypeError):
            obj = MenuReaderPDF(None)
            obj.openreader()

    def test_input_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            obj = MenuReaderPDF("FileNotExist.pdf")
            obj.openreader()

    def test_input_not_pdf(self):
        with self.assertRaises(FileTypeException):
            obj = MenuReaderPDF("FileNotPDF.txt")
            obj.openreader()


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()
