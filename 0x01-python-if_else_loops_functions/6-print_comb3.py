#!/usr/bin/python3
for n in range(0, 8):
    num_two = n + 1
    for t in range(num_two, 10):
        print("{:d}{:d}".format(n, t), end=", ")
print("{}".format("89"))
