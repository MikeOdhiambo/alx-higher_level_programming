#!/usr/bin/python3
""" A module defining a Rectangle class """


class Rectangle:
    """ Defines a Rectangle object

    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle
        number_of_instances(int): number of class instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes a rectangle instance

        Args:
            width(int): width
            height(int): height
        """
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ Prints a string representation of the rectangle"""
        str_rect = ""
        if self.__width == 0 or self.__height == 0:
            return str_rect
        for i in range(self.__height - 1):
            str_rect += "#" * self.__width + "\n"
        str_rect += "#" * self.__width
        return str_rect

    def __repr__(self):
        """Returns a string representation for recreating instance"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Prints a message when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
