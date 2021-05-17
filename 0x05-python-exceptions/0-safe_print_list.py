#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # copy_list = ""
    # for i in my_list[0:x]:
    #   copy_list += (str(my_list[i]))
    # print("{}".format(copy_list))
    element = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            element += 1
    except IndexError:
        # IndexError: trying to access an index that is invalid
        pass
    print("")
    return element
