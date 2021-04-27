#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
template_string = "Last digit of {} is {} and is {}"
if number >= 0:
    last_dgt = number % 10
    if last_dgt > 5:
        print(template_string.format(number, last_dgt, "greater than 5"))
    elif last_dgt < 6 != 0:
        print(template_string.format(number, last_dgt, "\
less than 6 and not 0"))
    else:
        print(template_string.format(number, last_dgt, "0"))
else:
    # convert a negative number to positive
    convert_negative = number * (-1)
    last_dgt = convert_negative % 10
    if last_dgt == 0:
        print(template_string.format(number, last_dgt, "0"))
    else:
        # the last digit is printed with "-" sign
        print(template_string.format(number, last_dgt * (-1), "\
less than 6 and not 0"))
