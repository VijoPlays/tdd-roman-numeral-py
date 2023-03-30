import re


romanNumerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def convertRomanToArabic(romanString):
    """Converts a string of Roman Numerals to an Arabic Number."""
    validateRomanString(romanString)

    # Init values
    result = 0
    previousNumber = 0

    i = 0
    while i < len(romanString):
        number = romanNumerals.get(romanString[i])

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
