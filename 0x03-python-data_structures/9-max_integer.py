#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    # Initially the first number in the list is the largest
    big_number = my_list[0]
    for n in my_list:
        # It goes through and compares each number, if it finds that is greater
        # than the one assigned in position 0 of the list, it automatically
        # assigns the number that meets that condition, the value of big_number
        if n > big_number:
            big_number = n
    return big_number
