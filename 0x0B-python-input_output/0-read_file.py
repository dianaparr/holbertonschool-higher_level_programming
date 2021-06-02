#!/usr/bin/python3
"""
Function that reads a text file
"""
def read_file(filename=""):
    """ Read file encoding utf-8 

    Parameters:
            filename: the file to open and read
    """
    with open(filename, mode='r', encoding='UTF8') as f:
        file_to_read = f.read()
    print("{}".format(file_to_read))
