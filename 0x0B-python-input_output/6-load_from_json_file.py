#!/usr/bin/python3
""" Function that function that
    creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ Use the module json and function
        json.load()

        Parameters:
                filename(string): the file to created

        * Only data type: string, integer, float,
          bool, list, dictionaries and None
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        string_json = json.load(f)
    return string_json
