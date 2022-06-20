#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    a, b = args
    res = 0
    try:
        res = fct(a, b)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        res = None
    return res
