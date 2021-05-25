#!/usr/bin/python3
from typing import Type


def print_square(size):
    for x in range(size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        for y in range(size):
            print('#', end="")
        print("")
