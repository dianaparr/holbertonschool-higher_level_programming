#!/usr/bin/python3
for n in range(00, 100):
    if n == 99:
        print("99")
    else:
        print("{:02d}".format(n), end=", ")
