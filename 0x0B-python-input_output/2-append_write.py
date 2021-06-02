#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """ Write in the file appending to the end
        of the file if it exists.

        Paramenters:
                filename(string): the file to write
                text(string): number of bytes to write with
                              mode append.
    """
    with open(filename, mode='a', encoding='UTF8') as f:
        file_to_append = f.write(text)
    return file_to_append
