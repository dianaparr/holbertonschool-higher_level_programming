#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that returns the new matrix with the
        result of the division.

        Parameters:
            matrix (lists of lists): of intergers or floats
            div (int or float): divider

        Return:
            matrix_result: new matrix with the results of
                           the division
    """
    matrix_result = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("\
matrix must be a matrix (list of lists) of integers/floats")
    for x in range(len(matrix)):
        if type(matrix[x]) is not list:
            raise TypeError("\
matrix must be a matrix (list of lists) of integers/floats")
        list_result = []
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) is not int and\
                    type(matrix[x][y]) is not float:
                raise TypeError("\
matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[x]) != len(matrix[0]):
                raise TypeError("\
Each row of the matrix must have the same size")
            else:
                list_result.append(round(matrix[x][y] / div, 2))
        matrix_result.append(list_result)
    return matrix_result
