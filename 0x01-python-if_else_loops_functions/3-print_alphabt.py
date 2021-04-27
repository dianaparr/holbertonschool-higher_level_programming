#!/usr/bin/python3
for a in range(97, 123):
    # print alphabet except q and e
    if (a == 113 or a == 101):
        continue
    print("{:c}".format(a), end="")
