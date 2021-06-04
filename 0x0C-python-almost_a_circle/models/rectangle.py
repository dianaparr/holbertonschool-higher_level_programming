#!/usr/bin/python3
"""
Created a class called Rectangle inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """ Constructor method to initialize the attribute of the
        instantiated object with four optionals parameters
        and call to the super class Base with id:

        Args:
            width: Is a private attribute
            height: Is a private attribute
            x: Is a private attribute
            y: Is a private attribute
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        # call the super class with id
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
    Private instance attributes, each with its own public
    getter and setter
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
