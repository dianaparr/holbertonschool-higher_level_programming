#!/usr/bin/python3
def uniq_add(my_list=[]):
    # convert to set my_list, no repeat sum of the elements
    list_two = set(my_list)
    sum_elem = 0
    for element in list_two:
        sum_elem += element
    return sum_elem
