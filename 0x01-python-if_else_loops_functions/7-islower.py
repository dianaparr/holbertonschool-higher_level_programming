#!/usr/bin/python3
def islower(c):
    # function ord(): return the UNICODE code of the chr given as argument
    if ord(c) in range(97, 123):
        return True
    else:
        return False
