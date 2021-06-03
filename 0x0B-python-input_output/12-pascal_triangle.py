#!/usr/bin/python3
"""
Function that representing the Pascal's triangle
"""


def pascal_triangle(n):
    """ Function that return a list of list of
        integers.

        Arguments:
                n(integer): Number of lines of the triangle
    """
    # list empty of the triangle
    list_triangle = list()

    if (n <= 0):
        return list_triangle

    # traverse each line of the triangle
    for i in range(1, n + 1):
        element = 1
        # list empty of the line
        list_line = list()
        # traverse each element of the line
        for e in range(1, i + 1):
            list_line.append(int(element))
            # equation
            element = element * (i - e) / e
        list_triangle.append(list_line)
    return list_triangle
