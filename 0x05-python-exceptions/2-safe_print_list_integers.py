#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0
    # inside a loop to use continue on exception
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            element += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return element
