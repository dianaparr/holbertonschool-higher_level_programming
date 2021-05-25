#!/usr/bin/python3
from typing import Type


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    for x in range(size):
        for y in range(size):
            print('#', end="")
        print("")
