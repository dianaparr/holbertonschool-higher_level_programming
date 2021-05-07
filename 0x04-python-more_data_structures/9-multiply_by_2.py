#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a copy of the dictionary, use copy() method
    dupli_dictionary = a_dictionary.copy()
    # Goes round the dictionary and for each key
    # multiplies it's value by two
    for value in dupli_dictionary:
        dupli_dictionary[value] *= 2
    return dupli_dictionary
