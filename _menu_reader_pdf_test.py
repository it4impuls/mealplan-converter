"""Tests für den MenuReader"""
import os
import logging
import unittest
from _menu_reader_pdf import MenuReaderPDF
from _exceptions import TableException, TableConditionException, FileTypeException


class TestMenuReaderPDF(unittest.TestCase):

    def test_input_is_none(self):
        with self.assertRaises(TypeError):
            obj = MenuReaderPDF(None)

    def test_input_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            obj = MenuReaderPDF("FileNotExist.pdf")

    def test_input_not_pdf(self):
        with self.assertRaises(FileTypeException):
            obj = MenuReaderPDF("FileNotPDF.txt")

    def test_table_not_exist(self):
        with self.assertRaises(TableException):
            obj = MenuReaderPDF("emptypdf.pdf")

    def test_table_condition(self):
        with self.assertRaises(TableConditionException):
            obj = MenuReaderPDF("tablenottherightcondition.pdf")


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()
