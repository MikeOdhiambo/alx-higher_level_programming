#!/usr/bin/python3
""" A module defining a Rectangle class """


class Rectangle:
    """ Defines a Rectangle object

    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initializes a rectangle instance

        Args:
            width(int): width
            height(int): height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
