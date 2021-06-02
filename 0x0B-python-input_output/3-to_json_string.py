#!/usr/bin/python3
""" Function that returns the JSON representation
    of an object 
"""
import json

def to_json_string(my_obj):
    """ Use the module json and function
        json.dumps()

        Parameters:
                my_obj(data type of Python*): object to be
                                       represented in JSON.

        * Only data type: string, integer, float,
          bool, list, dictionaries and None
    """
    string_json = json.dumps(my_obj)
    return string_json
