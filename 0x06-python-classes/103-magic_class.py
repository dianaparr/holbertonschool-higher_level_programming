#!/usr/bin/python3
""" Import the module math that provides access
    to the mathematical functions defined by the C standard """
import math
""" Find the circumference and area of a circle """


class MagicClass:
    """ Initialization of the MagicClass class with
        the radius parameter """
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
