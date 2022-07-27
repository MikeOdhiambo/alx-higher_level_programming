#!/usr/bin/python3
"""
This module contains the Base class for rectangle and square classes
"""
class Base:
    """ Define base class """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializes instance variables

        Args:
            id(int): Instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base._nb_objects
