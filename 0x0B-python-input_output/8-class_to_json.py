#!/usr/bin/python3
"""
Function that returns the dictionary description
"""


def class_to_json(obj):
    """ Use attribute magic __dict__

    Parameters:
            obj: the object
    """
    return obj.__dict__
