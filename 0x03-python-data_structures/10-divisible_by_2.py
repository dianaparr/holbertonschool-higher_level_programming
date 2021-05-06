#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_two = []
    for m in my_list:
        if m % 2 == 0:
            list_two.append(True)
        else:
            list_two.append(False)
        # Fill a empty list there: [True, False, True...]
    return list_two
