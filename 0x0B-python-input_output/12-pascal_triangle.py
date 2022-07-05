#!/usr/bin/python3
""" This module contains the function pascal_triangle """


def pascal_triangle(n):
    """
    Returns a Pascal's triangle in range n

        Args:
            n ('int') : size of triangle
    """
    if n <= 0:
        return []

    pat = [[0 for x in range(i + 1)] for i in range(n)]

    for i in range(n):
        pat[i][0] = 1
        for j in range(1, i + 1):
            if j < len(pat[i - 1]):
                pat[i][j] = pat[i - 1][j - 1] + pat[i - 1][j]
            else:
                pat[i][j] = 1
    return pat
