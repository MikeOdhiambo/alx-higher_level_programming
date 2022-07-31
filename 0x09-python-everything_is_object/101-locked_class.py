#!/usr/bin/python3
""" This module defines a locked class. """


class LockedClass:
    """
    Prevents dynamic creation of new instance attributes 
    other than first_name by user.
    """
    __slots__ = ['first_name']
