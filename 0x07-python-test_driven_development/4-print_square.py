#!/usr/bin/python3
"""
Function that prints a square
"""


def print_square(size):
    """ Function that prints a square with the
        character '#'.

        Parameter:
            size (int and positive): size length of the square.
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print('#', end="")
        print("")
