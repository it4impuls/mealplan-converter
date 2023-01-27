"""Tests für den MenuReader"""
import os
import logging
import unittest
from _allergenic import Allergenic
from _menu_reader_pdf import MenuReaderPDF
from _exceptions import AllergenicException


class TestAllergenic(unittest.TestCase):
    ALLERGENIC_STRING_01 = """Zusatzstoffe: (1) mit Konservierungsstoff*;"""
    ALLERGENIC_STRING_02 = """Zusatzstoffe: (1) mit Konservierungsstoff*; (2) mit Antioxidationsmittel*; (6) mit einer Zuckerart und Süßungsmittel*; (12) mit Farbstoff*; (13) geschwefelt*; (14) gewachst*   Allergene: (a) Glutenhaltiges Getreide und -erzeugnisse; (c) Eier und -erzeug-
    nisse; (d) Fisch und -erzeugnisse; (f) Soja und -erzeugnisse; (g) Milch und -erzeugnisse; (i) Sellerie und -erzeugnisse; (k) Senf und -erzeugnisse; (m) Schwefeldioxid und Sulfide in einer Konzentration von mehr als 10mg/kg oder 10/mg/l, 
    als SO2 angegeben; (p) Laktose; (a-1) Weizen und Weizenerzeugnisse; (a-5) Gerste und Gersteerzeugnisse   [* Kennzeichnung gesetzlich vorgegeben]"""

    def test_no_allergenics(self):
        with self.assertRaises(AllergenicException):
            obj = Allergenic(None)

    @unittest.skip("Funktioniert noch nicht")
    def test_empty_allergenics(self):
        obj = Allergenic("").get_allgernics()
        self.assertDictEqual(obj, dict())

    def test_allergenics_string_01(self):
        obj = Allergenic(TestAllergenic.ALLERGENIC_STRING_02).get_allgernics()


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(message)s',
        level=logging.DEBUG
    )
    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
    unittest.main()
