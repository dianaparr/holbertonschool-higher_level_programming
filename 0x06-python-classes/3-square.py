#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    # class method. Access to attribute with self.__size
    def area(self):
        return self.__size ** 2
