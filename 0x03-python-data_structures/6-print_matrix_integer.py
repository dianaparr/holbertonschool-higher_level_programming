#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            # -1 is to stop in the last position
            if len(matrix[x]) - 1 > y:
                print("{:d} ".format(matrix[x][y]), end="")
            else:
                print("{:d}".format(matrix[x][y]), end="")
        print("")
