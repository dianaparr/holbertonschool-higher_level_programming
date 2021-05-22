#!/usr/bin/python3
""" Create a class called LockedClass """


class LockedClass:
    """ Use of the magic method __slots__ by
        defining a list with the attribute you
        want to create.

        This method is used to avoid the dynamic
        creation of attrubutes """
    __slots__ = ["first_name"]
