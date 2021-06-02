#!/usr/bin/python3
"""
Function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """ Write in the file
        Create the file if doesn't exist and
        Overwrite the content of the file if it
        already exists.

        Paramenters:
                filename(string): the file to write
                text(string): number of bytes to write
    """
    with open(filename, mode='w+', encoding='UTF8') as f:
        file_to_write = f.write(text)
    return file_to_write
