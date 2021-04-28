#!/usr/bin/python3
def remove_char_at(str, n):
    # create a string empty
    str_new = ""
    for idx in range(0, len(str)):
        if idx != n:
            str_new += str[idx]
    return str_new
