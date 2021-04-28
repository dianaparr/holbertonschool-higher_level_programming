#!/usr/bin/python3
for a in range(122, 96, -1):
    # To capitalize one yes and no in the other one
    if a % 2 == 0:
        c = a
    else:
        c = a - 32
    print("{:c}".format(c), end="")
