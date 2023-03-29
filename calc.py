import re


class RomanNumeralConverted:
    """An object that contains values to convert a Roman letter to an Arabic counterpart."""

    def __init__(self, roman, arabic, precedingLetter):
        self.roman = roman
        """The Roman letter."""
        self.arabic = arabic
        """The Arabic value for the roman letter."""
        self.precedingLetter = precedingLetter
        """The Roman letter that is allowed to be before this letter."""

    def isSmaller(currentLetter):
        """Checks that the currentLetter is smaller than the precedingLetter."""


romanNumerals = {
    "I": RomanNumeralConverted(roman="I", arabic=1, precedingLetter=""),
    "V": RomanNumeralConverted(roman="V", arabic=5, precedingLetter="I"),
    "X": RomanNumeralConverted(roman="X", arabic=10, precedingLetter="I"),
    "L": RomanNumeralConverted(roman="L", arabic=50, precedingLetter="X"),
    "C": RomanNumeralConverted(roman="C", arabic=100, precedingLetter="X"),
    "D": RomanNumeralConverted(roman="D", arabic=500, precedingLetter="C"),
    "M": RomanNumeralConverted(roman="M", arabic=1000, precedingLetter="C"),
}


def convertRomanToArabic(romanString):
    """Converts a string of Roman Numerals to an Arabic Number."""
    validateRomanString(romanString)

    # Init values
    result = 0
    previousNumber = 0

    i = 0
    while i < len(romanString):
        number = romanNumerals.get(romanString[i]).arabic

        # Since we always add 'number', we need to check if 'previousNumber' should have been subtracted based on the rules of roman numerals. If it was, we have to subtract it twice (once to negate it, twice to make it a subtraction, instead of negation).
        if number > previousNumber:
            result = result - previousNumber * 2

        # Set new init values
        result += number
        previousNumber = number
        i += 1

    return result


def validateRomanString(romanString):
    """Validates a string of Roman characters."""

    """
        Regex explanation: 
            ^ = Match with first character in string.
            x{n,m} = x needs to appear between n and m times.
            () = Simple grouping of expression, similar to mathematics.
            | = Or
            ? = Expressions following it are optional.
                -> (IX|IV|V?I{0,3}) == Find IX OR IV OR V with OPTIONAL 0 to 3 Is
            $ = Match with last character in string.

    """
    regex = bool(
        re.search(
            r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", romanString
        )
    )
    if regex == False:
        raise Exception("Roman string was not valid, recheck please!")
    return
