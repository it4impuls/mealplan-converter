""" Benötigte Module. """
import os
import logging
import coloredlogs
import unittest
from _menu_reader_pdf import MenuReaderPDF

class TestMenuReaderPDF(unittest.TestCase):

    def test_input_is_none(self):
        with self.assertRaises(Exception):
            obj = MenuReaderPDF(None)

if __name__ == "__main__":
    logger = logging.getLogger()
    coloredlogs.install(level='DEBUG')
    coloredlogs.install(level='DEBUG', logger=logger)
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()
