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
        self.__width = width
        # super().__init__(name, value)
        super().integer_validator("width", width)
        self.__height = height
        super().integer_validator("height", height)
