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
    state = True
    i = 0
    while i in range(len(text)):
        # remove spaces at the begginning
        if text[i] == " " and state is True:
            i += 1
            continue
        # remove spaces at the end
        elif text[i] == " " and text[i + 1] == " ":
            state = True
            i += 1
            continue
        # remove spaces before the line break
        elif text[i] == '?' or text[i] == '.' or text[i] == ':':
            state = False
            print("{}{}".format(text[i], '\n'))
            i += 2
        else:
            state = False
            print("{}".format(text[i]), end="")
            i += 1
