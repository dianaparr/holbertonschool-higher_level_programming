#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    length_arg = len(argv)
    if length_arg == 2:
        print("{} {}".format((length_arg - 1), "argument:"))
        print("{}: {}".format(1, argv[1]))
    elif length_arg == 1:
        print("{} {}".format((length_arg - 1), "arguments."))
    else:
        print("{} {}".format((length_arg - 1), "arguments:"))
        for c in range(1, length_arg):
            print("{}: {}".format(c, argv[c]))
