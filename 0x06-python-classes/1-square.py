#!/usr/bin/python3
""" A module for the Square class """


class Square:
    """
    A Square class definition

    Attributes:
        size(int): Length of side of square
    """

    def __init__(self, size):
        """
        Initialize the Square class

        Args:
            size (int): Length of side of square
        """
        self.__size = size
