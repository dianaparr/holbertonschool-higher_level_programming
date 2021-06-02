#!/usr/bin/python3
"""
Function that indicate object is
an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Parameters:
        obj: object to evaluate
        a_class: possible class to witch obj

    Return:
        True: if the object is an instance
              of the specified class that inherited,
              otherwise False.
    """
    #  type(obj) the class of the object
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
