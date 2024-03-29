#!/usr/bin/python3
""" Base class providing a prototype for inheriting classes """
import JSON
import turtle


class Base:
    """ Defines a super class for subsequent classes """
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
            self.id = Base.__nb_objects
