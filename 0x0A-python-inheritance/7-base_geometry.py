#!/usr/bin/python3
""" Defines a Geometry module """


class BaseGeometry:
    """ A class that defines basic Geometry operations"""

    def area(self):
        """ Give an error message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Returns True if value is an integer, False otherwise"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
