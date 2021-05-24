#!/usr/bin/python3
"""
Function that addition integers
"""


def add_integer(a, b=98):
    """ Function that returns the sum of two integers

        Parameters:
            a (int): a number int
            b=98 (int): another number int

        Returns:
            casted_numbers: casted to integers if they
                            are float and return addition
                            of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        casted_numbers = a + b
        return casted_numbers
