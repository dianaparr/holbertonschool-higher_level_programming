#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        # Use del() statement
        del a_dictionary[key]
    return a_dictionary
