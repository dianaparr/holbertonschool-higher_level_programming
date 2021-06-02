#!/usr/bin/python3
""" Function that returns an object represented
    by a JSON string
"""
import json


def from_json_string(my_str):
    """ Use the module json and function
        json.loads()

        Parameters:
                my_obj(data type of Python*): object represented
                                              by a JSON string

        * Only data type: string, integer, float,
          bool, list, dictionaries and None
    """
    py_object = json.loads(my_str)
    return py_object
