#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    arr_len = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(arr_len):
            if j < arr_len - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print()
