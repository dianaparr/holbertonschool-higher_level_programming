#!/usr/bin/python3
""" Define a class called Square """


class Square:
    """ Constructor method to initialize the attributes of the
    instantiated object 'size' """
    def __init__(self, size=0):
        """ validate the 'size' attribute with several conditions """
        # other way: type(size) != int
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
