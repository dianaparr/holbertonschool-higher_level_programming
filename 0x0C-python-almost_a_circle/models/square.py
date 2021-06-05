#!/usr/bin/python3
"""
Created a class called Square inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Constructor method to initialize the attribute of the
        instantiated object with four optionals parameters
        and call to the super class Rectangle with id, x, y, width and height:

        Args:
            size: assigned to width and height
            Use all attributes of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overrinding the special method __str__ """
        return "[{}] ({}) {}/{} - {}".format(__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    """
    Private instance attribute, with public
    getter and setter
    """
    @property
    def size(self):
        return self.width

    """
    Update attribute width
    raising exception:
        - TypeError if the input is not an integer
        - ValueError if width is under or equals 0
    """
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
            self.height = size
