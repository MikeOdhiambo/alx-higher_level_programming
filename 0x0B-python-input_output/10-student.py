#!/usr/bin/python3
""" This module contains the class Student """


class Student:
    """
    Student class

        Attributes:
            first_name ('str') : first name
            last_name ('str') : last name
            age ('int') : age
    """

    def __init__(self, first_name, last_name, age):
        """ Initializing attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of an instance
            Args:
                self(class) : refers to student
                attrs('str') : list of attributes (strings)
        """
        if type(attrs) is not list:
            return self.__dict__
        for attribute in attrs:
            if type(attribute) is not str:
                return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}