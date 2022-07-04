#!/usr/bin/python3
"""Determines if class is inherited from another class """


def is_kind_of_class(obj, a_class):
    """
    Checks if object is inherited from a_class its parents

    Args:
        obj(object): Object to check
        a_class(object): Class to check from
    """
    return issubclass(type(obj), a_class)
