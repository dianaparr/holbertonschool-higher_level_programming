#!/usr/bin/python3
""" Script that adds all arguments to
    a Python list 
"""

from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f_name = "add_item.json"
# first step: open file for read
list_argv = load_from_json_file(f_name)
