#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_my_list = len(my_list)
    if idx < 0 or idx >= len_my_list:
        return my_list
    # del statement can be used to delete an item at a given index
    del my_list[idx]
    return my_list
