#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_my_list = len(my_list)
    if idx < 0 or idx > len_my_list:
        return my_list
    else:
        # Create a copy of the list original, my_list[:]
        # represents the complete list
        list_two = []
        for e in range(0, len_my_list):
            if e == idx:
                list_two.append(element)
            else:
                list_two.append(my_list[e])
        return list_two
