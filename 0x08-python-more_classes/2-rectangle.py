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
        """ Sets the value of width

        Args:
            value(int): New width
        """
        if type(value) != int:
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
        """ Sets the value of height
        Args:
            value(int): New height
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
