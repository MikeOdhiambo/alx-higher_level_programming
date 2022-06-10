#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for item in matrix:
        square = list(map(lambda x: x * x, item))
        sq_matrix.append(square)
    return sq_matrix
