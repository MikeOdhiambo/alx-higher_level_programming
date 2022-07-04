#!/usr/bin/python3
""" Defines a Geometry module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Extends the BaseGeometry class """

    def __init__(self, width, height):
        """
        Initialize Rectangle class

        Args:
            width(int): Rect width
            height(int): Rect height
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """ Returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return a string representation of instance """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
