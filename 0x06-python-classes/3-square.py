#!/usr/bin/python3
""" Define a class called Square """


class Square:
    """ Constructor method to initialize the attributes of the
    instantiated object 'size' """
    def __init__(self, size=0):
        """ validate the 'size' attribute with several conditions """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    # class method. Access to attribute with self.__size
    def area(self):
        """ This class method returns the square of what is
            in the attribute 'size' """
        return self.__size ** 2
