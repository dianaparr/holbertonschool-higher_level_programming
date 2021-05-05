#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_my_list = len(my_list)
    if idx < 0 or idx > len_my_list:
        return my_list
    else:
        # Create a copy of the list original, my_list[:]
        # represents the complete list
        list_two = my_list[:]
        list_two[idx] = element
        return list_two
