#!/usr/bin/python3
"""
Create a class called Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ Constructor method to initialize the attribute of the
        instantiated object with two optionals parameters:

        Args:
            param1 (first_name): Is a public attribute, type str
            param2 (last_name): Is a public attribute, type str
            param2 (age): Is a public attribute, type str
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Public method that retrieves a dictionary representation
        of a Student instance
    """
    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return self.__dict__
        else:
            dict_json = dict()
            for a in attrs:
                # attributes instance list strings
                if a in self.__dict__:
                    # return dictionary representation
                    dict_json[a] = self.__dict__[a]
            return dict_json
