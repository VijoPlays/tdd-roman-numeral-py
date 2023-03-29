import unittest

import calc

# TODO: Look for library/annotations to make tests prettier (naming, etc)


# TODO: Later on: Tests for invalid input
# TODO: Test for C, L, M
# TODO: Disable VIIIV = 11


class TestRomanNumeralConverterHappyPath(unittest.TestCase):
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

    def test_XEquatesTo10(self):
        self.assertEqual(10, calc.convertRomanToArabic("X"))

    def test_IXEquatesTo9(self):
        self.assertEqual(9, calc.convertRomanToArabic("IX"))

    def test_XIEquatesTo11(self):
        self.assertEqual(11, calc.convertRomanToArabic("XI"))


# TODO: Proper exceptions: No Roman Characters, V before X (smaller char), VII IV (mix of smaller number and bigger number)
class TestRomanNumeralConverterUnhappyPath(unittest.TestCase):
    # def test_IVCanNotComeAfterVII(self):
    #     self.assertRaises(Exception, calc.convertRomanToArabic("VIIIV"))

    def test_VCanNotComeBeforeX(
        self,
    ):  # TODO: Do assertion of previousNumber next: raise Exception("")
        self.assertRaises(Exception, lambda: calc.convertRomanToArabic("VX"))


if __name__ == "__main__":
    unittest.main()
