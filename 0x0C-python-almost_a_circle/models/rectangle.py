#!/usr/bin/env python3
""" rectangle.py """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class

    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle
        x(int): x offset of rectangle
        y(int): y offset of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of Rectangle """
        super().__init__(id)
        self.width = width
        self.heigh = height
        self.x = x
        self.y = y

    def check_val(self, attrbt, value):
        """
        Validates the type and range of attributes

        Args:
            attrbt(int): Attribute to validate
            value(int): Value of the attribute
        """
        if type(value) is not int:
            raise TypeError(attrbt + "must be an integer")
        elif attrbt is "width" or attrbt is "height":
            if attrbt <= 0:
                raise ValueError(attrbt + "must be > 0")
        elif attrbt is "x" or attrbt is "y":
            if attrbt < 0:
                raise ValueError(attrbt + "must be >= 0")

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the value for width """
        self.check_val("width", value)
        self.__width = value

    @property
    def height(self):
        """ Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the value for height """
        self.check_val("height", value)
        self.__height = value

    @property
    def x(self):
        """ Get x """
        return self.__x

    @width.setter
    def x(self, value):
        """ Set the value for x """
        self.check_val("x", value)
        self.__x = value

    @property
    def y(self):
        """ Get y """
        return self.__y

    @width.setter
    def y(self, value):
        """ Set the value for y """
        self.check_val("y", value)
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height
