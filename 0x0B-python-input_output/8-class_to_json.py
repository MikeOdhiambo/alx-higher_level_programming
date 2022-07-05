#!/usr/bin/python3
""" This module contains the function class_to_json """


def class_to_json(obj):
    """ Return dict description of a class instance """
    return obj.__dict__
