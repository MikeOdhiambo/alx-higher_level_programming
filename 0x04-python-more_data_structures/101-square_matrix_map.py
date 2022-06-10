#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda itm: list(map(lambda x: x ** 2, itm)), matrix))
