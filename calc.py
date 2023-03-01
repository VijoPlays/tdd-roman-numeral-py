
# Converts a string of Roman Numerals to an Arabic Number.
def convertRomanToArabic(romanString):
    result = 0
    
    i = 0
    previousNumber = 0
    while i < len(romanString):
        number = calculateValue(romanString[i])

        # Since we always add 'number', we need to check if 'previousNumber' should have been subtracted based on the rules of roman numerals. If it was, we have to subtract it twice (once to negate it, twice to make it a subtraction, instead of negation).
        if number > previousNumber:
            result = result - previousNumber*2 

        result += number
        previousNumber = number
        i += 1

    return result 

# Calculates an arabic value of a single character.
def calculateValue(romanCharacter):
    result = 0

    if(romanCharacter == "I"):
        result = 1
    elif(romanCharacter == "V"):
        result = 5

    return result