#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            # convert str to int
            c = ord(s)
            # convert lower to upper
            s = chr(c - 32)
        print(s, end="")
    print("")
