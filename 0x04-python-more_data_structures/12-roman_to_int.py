#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == "" or not isinstance(roman_string, str):
        return 0
    else:
        dir_roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
        resul = 0
        length_roman_string = len(roman_string)
        for r in range(0, length_roman_string):
            # r + 1 is position next to first position, i.e., r.
            second = r + 1
            if second != length_roman_string and dir_roman[roman_string[r]]\
               < dir_roman[roman_string[second]]:
                resul = resul - dir_roman[roman_string[r]]
            else:
                resul = resul + dir_roman[roman_string[r]]
        return resul
