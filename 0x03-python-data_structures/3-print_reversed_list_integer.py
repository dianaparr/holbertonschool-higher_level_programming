#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # reverse() method: directly modifies the original list
    my_list.reverse()
    for element in my_list:
        print("{:d}".format(element))
