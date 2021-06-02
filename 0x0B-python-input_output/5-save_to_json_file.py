#!/usr/bin/python3
""" Function that writes an Object to
    a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Use the module json and function
        json.dumps() because object should be a
        JSON representation

        Parameters:
                my_obj(data type of Python*): object to be
                                       represented in JSON.
                filename(string): the file to write

        * Only data type: string, integer, float,
          bool, list, dictionaries and None
    """
    with open(filename, mode='w', encoding='UTF8') as f:
        string_json = json.dump(my_obj, f)
    return string_json
