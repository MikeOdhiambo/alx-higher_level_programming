#!/usr/bin/python3
"""
This module adds an attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """ Add attribute to object """
    if getattr(obj, "__dict__", None) is None:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
