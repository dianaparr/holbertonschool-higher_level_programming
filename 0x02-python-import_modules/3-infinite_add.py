#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length_arg = len(argv)
    sum_arg = 0
    for c in range(1, length_arg):
        sum_arg += int(argv[c])
    print("{}".format(sum_arg))
