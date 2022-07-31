#!/usr/bin/python3
""" Square class that inherits from the Rectangle class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square class with Rectangle as a superclass

    Attributes:
        size(int): length of one side
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square instance

        Args:
            size(int): length of one side
            x(int): x offset
            y(int): y offset
            id(int): identifying number
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Print string representation of a Square instance """

        rep = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.__width)
        return rep

    @property
    def size(self):
        """ Find size attribute """
        return self.__width

    @size.setter
    def size(self, value):
        """ Set size attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ Update square with new attributes """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                setattr(self, 'id', args[0])
            if len(args) > 1:
                setattr(self, 'size', args[1])
            if len(args) > 2:
                setattr(self, 'x', args[2])
            if len(args) > 3:
                setattr(self, 'y', args[3])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
