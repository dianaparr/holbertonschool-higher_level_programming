#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use list comprehension and map() function
    matrix_two = [list(map(lambda n: n**2, x)) for x in matrix]
    return matrix_two
