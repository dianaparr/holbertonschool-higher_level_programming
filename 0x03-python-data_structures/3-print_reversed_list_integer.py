#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == 0:
        print("{}".format(""))
    # reverse() method: directly modifies the original list
    my_list.reverse()
    for element in my_list:
        print("{:d}".format(element))
