#!/usr/bin/python3
"""
Function that indicate object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Parameters:
        obj: object to evaluate
        a_class: possible class to witch obj

    Return:
        True: if the object is exactly an instance
              of the specified class,
              otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
