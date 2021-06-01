#!/usr/bin/python3
"""
Function that indicate object is
an instance of, or if the object is an
instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Parameters:
        obj: object to evaluate
        a_class: possible class to witch obj

    Return:
        True: if the object is an instance
              of the specified class,
              otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
