import unittest

import calc

#TODO: Look for library/annotations to make tests prettier (naming, etc)


#TODO: Later on: Tests for invalid input
#TODO: Test for X, C, L, M
#TODO: Disable VIIIV = 11

class TestRomanNumeralConverter(unittest.TestCase):
    def test_IEquatesTo1(self):
        self.assertEqual(1, calc.convertRomanToArabic("I"))

    def test_IIEquatesTo2(self):
        self.assertEqual(3, calc.convertRomanToArabic("III"))

    def test_VEquatesTo5(self):
        self.assertEqual(5, calc.convertRomanToArabic("V"))

    def test_VIEquatesTo6(self):
        self.assertEqual(6, calc.convertRomanToArabic("VI"))

    def test_IVEquatesTo4(self):
        self.assertEqual(4, calc.convertRomanToArabic("IV"))

    def test_IVEquatesTo40(self):
        self.assertEqual(11, calc.convertRomanToArabic("VIIIV"))

if __name__ == '__main__':
    unittest.main()