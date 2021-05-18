#!/usr/bin/python3
from typing import Type


class Square:
    def __init__(self, size=0):
        # other way: type(size) != int
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
