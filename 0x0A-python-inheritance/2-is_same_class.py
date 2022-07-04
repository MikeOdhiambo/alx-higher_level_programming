#!/usr/bin/python3
""" This module determines the instance of an object """


def is_same_class(obj, a_class):
    """ Returns True if object is instance of a_class, False otherwise"""
    return (type(obj).__name__ == a_class.__name__)
