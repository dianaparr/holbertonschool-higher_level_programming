#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            # convert str to int
            conv = ord(c)
            # convert lower to upper
            c = chr(conv - 32)
        print("{}".format(c), end="")
    print("")
