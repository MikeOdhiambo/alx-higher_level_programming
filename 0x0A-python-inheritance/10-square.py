#!/usr/bin/python3
""" Defines a Square module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Extends the Rectangle class """

    def __init__(self, size):
        """
        Initialize Rectangle class

        Args:
            width(int): Rect width
            height(int): Rect height
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
