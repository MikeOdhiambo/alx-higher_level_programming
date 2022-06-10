#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    sq = list(map(lambda outer: list(
        map(lambda inner: inner ** 2, outer)), matrix))
    return sq
