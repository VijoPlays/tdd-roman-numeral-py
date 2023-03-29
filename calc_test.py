import unittest

import calc

# TODO: Look for library/annotations to make tests prettier (naming, etc)


class TestRomanNumeralConverterHappyPath(unittest.TestCase):
    def test_IEquatesTo1(self):
        """
        I must equal 1.
        """
        self.assertEqual(1, calc.convertRomanToArabic("I"))

    def test_IIEquatesTo2(self):
        """
        I works with addition: III must equal 3.
        """
        self.assertEqual(3, calc.convertRomanToArabic("III"))

    def test_VEquatesTo5(self):
        """
        V must equal 5.
        """
        self.assertEqual(5, calc.convertRomanToArabic("V"))

    def test_IVEquatesTo4(self):
        """
        V works with subtraction: IV must equal 4.
        """
        self.assertEqual(4, calc.convertRomanToArabic("IV"))

    def test_VIEquatesTo6(self):
        """
        V works with addition: VI must equal 6.
        """
        self.assertEqual(6, calc.convertRomanToArabic("VI"))

    def test_XEquatesTo10(self):
        """
        X must equal 10.
        """
        self.assertEqual(10, calc.convertRomanToArabic("X"))

    def test_IXEquatesTo9(self):
        """
        X works with subtraction: IX must equal 9.
        """
        self.assertEqual(9, calc.convertRomanToArabic("IX"))

    def test_XIEquatesTo11(self):
        """
        X works with addition: XI must equal 11.
        """
        self.assertEqual(11, calc.convertRomanToArabic("XI"))


class TestRomanNumeralConverterUnhappyPath(unittest.TestCase):
    def test_IIVIsNotValid(self):
        """
        Certain letter combinations are not valid: IIV is not valid.
        """
        self.assertRaises(Exception, lambda: calc.convertRomanToArabic("IIV"))

    def test_VCanNotComeBeforeX(self):
        """
        Certain letter combinations are not valid: V cannot come before X.
        """
        self.assertRaises(Exception, lambda: calc.convertRomanToArabic("VX"))

    def test_IIIIIIINotValid(self):
        """
        Numbers cannot repeat: IIIIIII is not a valid Roman string.
        """
        self.assertRaises(Exception, lambda: calc.convertRomanToArabic("IIIIIII"))

    def test_IVCanNotComeAfterVII(self):
        """
        Numbers cannot repeat: VI can not be followed by IV.
        """
        self.assertRaises(Exception, lambda: calc.convertRomanToArabic("VIIV"))


if __name__ == "__main__":
    unittest.main()
