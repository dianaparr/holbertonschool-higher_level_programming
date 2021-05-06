#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Use of the sorted() function built-in
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary.get(i)))
