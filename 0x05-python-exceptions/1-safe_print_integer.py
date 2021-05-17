#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        # if value is not int:
        return False
    except TypeError:
        return False
