#!/usr/bin/python3
def print_last_digit(number):
    last_dgt = number % 10
    if number >= 0:
        print("{:d}".format(last_dgt), end="")
        return last_dgt
    else:
        # convert a negative number to positive
        convert_negative = number * (-1)
        last_dgt = convert_negative % 10
        print("{:d}". format(last_dgt), end="")
        return last_dgt
