#!/usr/bin/python3
"""
Define a class called MyList that inherits from list
"""


class MyList(list):
    """ 
    Declare a public instance method 
    """
    def print_sorted(self):
        """ Function that prints the list sorted 

            Parameters:
                    self: iterable object

            Use function sorted(): function returns a
            sorted list of the specified iterable object
        """
        print(sorted(self))
