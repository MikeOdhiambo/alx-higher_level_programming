#!/usr/bin/python3
""" Checks if an object is an instance of a class """


def inherits_from(obj, a_class):
    """
    Returns True if obj is instance of a_class (directly or indirectly

    Args:
        obj(obj): Object item to check
        a_class(obj): Class object to check against
    """
    return (not type(obj) is a_class and issubclass(type(obj), a_class))
