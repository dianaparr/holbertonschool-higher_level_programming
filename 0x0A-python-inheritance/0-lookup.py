#!/usr/bin/python3
"""
Function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """ Parameters:
            obj: object

        Returns:
            list object
    """
    return dir(obj)
