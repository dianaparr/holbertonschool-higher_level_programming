#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        numerator = 0
        denominator = 0
        for t in my_list:
            # The tuples above are added together and
            # each one is performing a multiplication
            numerator += t[0] * t[1]
            # It is the sum of the second elements of
            # each tuple
            denominator += t[1]
        return numerator / denominator
    return 0
