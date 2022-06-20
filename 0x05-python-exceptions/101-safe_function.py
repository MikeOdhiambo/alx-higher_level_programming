#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    a, b = args
    res = 0
    try:
        res = fct(a, b)
        return res
    except Exception as err:
        sys.stderr.write("Exception: {}".format(err))
        res = None
