#!/usr/bin/python3
""" Define a class called Square """


class Square:
    """ Constructor method to initialize the attributes of the
        instantiated object 'size' """
    def __init__(self, size=0):
        self.size = size

    # getter method that retrieves the value of the attribute
    @property
    def size(self):
        return self.__size

    # setter method that sets the value
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ This class method returns the square of what is
            in the attribute 'size' """
        return self.__size ** 2
