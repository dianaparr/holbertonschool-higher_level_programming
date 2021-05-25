#!/usr/bin/python3
"""
Function that prints a string
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints a strings preceded by the
        phrase: 'My name is <first_name> <last_name>'

        Parameters:
            first_name (string): first part of the sentence
            last_name="" (string): second part of the sentence
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
