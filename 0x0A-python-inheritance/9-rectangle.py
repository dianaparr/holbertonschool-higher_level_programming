#!/usr/bin/python3
"""
Created a Class Rectangle and import module of class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Constructor method to initialize the attribute of the
        instantiated object with two optionals parameters
        to be validated by integer_validator:

        Args:
            param1 (width): Is a private attribute
            param2 (height): Is a private attribute
    """
    def __init__(self, width, height):
        # super().__init__(name, value)
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    """ Public instance method that return
        the area of a rectangle
    """
    def area(self):
        return self.__width * self.__height

    """ Use of the special method __str__ that returns a string
        with what you want to show, for example, to an end user """
    def __str__(self):
        show_mssg = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return show_mssg
