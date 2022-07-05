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
        """ Initialize an instance """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        " Returns a dictionary representation of an instance "
        return self.__dict__
