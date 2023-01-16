import unittest
import converter

class TestConverter(unittest.TestCase):

    def testConverterBothArgumentsNone(self):
        with self.assertRaises(Exception):
            converter.Converter.convert(None,None)
    
    def testInputNotPresent(self):
        with self.assertRaises(FileNotFoundError):
            converter.Converter.convert("fakeNoneExistent.pdf", None)

if __name__ == '__main__':
    unittest.main()