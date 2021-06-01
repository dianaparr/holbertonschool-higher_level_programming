#!/usr/bin/python3
"""
Created a Class Square and import module (inherits from) of class Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Constructor method to initialize the attribute of the
        instantiated object with one option parameter
        to be validated by integer_validator:

        Args:
            param1 (size): Is a private attribute
    """
    def __init__(self, size):
        # super().__init__(name, value)
        super().integer_validator("size", size)
        self.__size = size

    """ Public instance method that return
        the area of a square
    """
    def area(self):
        return self.__size ** 2

    """ Use of the special method __str__ that returns a string
        with what you want to show, for example, to an end user """
    def __str__(self):
        show_mssg = "[Square] {}/{}".format(self.__size, self.__size)
        return show_mssg

