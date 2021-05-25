#!/usr/bin/python3
"""
Function that prints a text
"""


def text_indentation(text):
    """ Function that prints a text with two lines
        after each of these characters: '.', '?' and ':'

        Parameters:
            text (str): text with the sentence or paragraph
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i in range(len(text)):
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print("{}{}".format(text[i], '\n'))
            i += 1
        else:
            print("{}".format(text[i]), end="")
        i += 1
