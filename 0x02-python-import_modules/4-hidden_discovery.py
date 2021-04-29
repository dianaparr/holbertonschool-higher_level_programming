#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    # function dir() returns an ordered list of strings containing
    # the names defined by a module
    names = dir(hidden_4)
    names_length = len(names)
    for n in range(0, names_length):
        if names[n][0] != "_":
            print("{}".format(names[n]))
