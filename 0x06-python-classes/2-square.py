#!/usr/bin/python3
""" A simple module with the Square class """


class Square:
    """
    A Square class definition

    Attributes:
        size(int): Length of side of square
    """

    def __init__(self, size=0):
        """
        Initialize the Square class

        Args:
            size (int): Length of side of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
