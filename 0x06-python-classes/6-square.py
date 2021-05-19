#!/usr/bin/python3
""" Define a class called Square """


class Square:
    """ Constructor method to initialize the attributes of the
        instantiated object 'size' and 'position' """
    def __init__(self, size=0, position=(0, 0)):
        """

        Args:
            param1 (__size): Is a private attribute, type int
            param2 (position): Is a private attribute, is a tuple and int
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        for t in value:
            # conditions: type tuple, to integers positives (t > 0)
            if type(t) is not int or len(value) != 2\
                 or t < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    def area(self):
        """ This class method returns the square of what is
            in the attribute 'size' """
        return self.__size ** 2

    def my_print(self):
        """ This class method prints in stdout the square
            with the character '#'.

            Is a nested loop for printing.

            The print range will be up to the value of
            the private attribute '__size'

            Add condition if position in index 1 is greater than zero """
        if self.__position[1] > 0:
            for i in range(0, self.__position[1]):
                print("")
        for x in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
