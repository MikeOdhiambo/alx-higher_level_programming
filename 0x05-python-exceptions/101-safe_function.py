#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    a, b = args
    res = 0
    try:
        res = fct(a, b)
        return res
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
