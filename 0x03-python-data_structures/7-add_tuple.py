#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = (0, 0)
    tp_a = tuple_a + tup
    tp_b = tuple_b + tup
    return tp_a[0] + tp_b[0], tp_a[1] + tp_b[1]
