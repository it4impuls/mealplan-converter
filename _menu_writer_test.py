""" Module. """
import os
import logging
import unittest
from _exceptions import MenuWriterException


class TestMenuWriter(unittest.TestCase):

    def test_object_created(self):
        with self.assertRaises(Exception):
            pass


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()