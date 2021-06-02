#!/usr/bin/python3
"""
Function that adds a new attribute to
an object if it’s possible
"""


def add_attribute(obj, element, value):
    """ Use functions built-ins like hasattr() and setattr() """
    if not hasattr(obj, '__dict__'):
        # __dict__ lists the attributes of a class
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, element, value)
