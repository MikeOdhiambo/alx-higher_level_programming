#!/usr/bin/python3
""" A Rectangle class that inherits from the Base class """
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
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get x attr """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x attr """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get y attr """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y attr """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with # """
        print("\n" * (self.__y), end="")
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ Print a string representation of a Rectangle instance """
        rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return rep
