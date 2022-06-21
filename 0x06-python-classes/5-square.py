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
        self.__size = size

    @property
    def size(self):
        """ Modifies the size of the square """
        return self.__size

    @size.setter
    def size(self, size):
        """ Modifies the size of the square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a square

        Returns:
            int: Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square in # chars"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
