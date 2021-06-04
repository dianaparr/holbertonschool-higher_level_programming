#!/usr/bin/python3
"""
Created a class called Base
"""


class Base:
    """ This class will be the "base" of all other
        classes in this project.

        Purpose: manage id attribute in all classes
                 and to avoid duplicating the same code.

        Created of private class attribute called __nb_objects = 0
        which will be a 'counter' that will provide the id in case
        it is found.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method to initialize the attribute of the
        instantiated object with one parameter:

        Parameter:

            id (integer): Is a public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
