#!/usr/bin/python3
"""
Function that divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """ """
    matrix_result = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for x in range(len(matrix)):
        list_result = []
        for y in range(len(matrix[x])):
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(matrix[x]) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            else:
                list_result.append(round(matrix[x][y] / div, 2))
        matrix_result.append(list_result)
    return matrix_result
    