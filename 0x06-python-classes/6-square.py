#!/usr/bin/python3
""" A simple module with the Square class """


class Square:
    """
    A Square class definition

    Attributes:
        size(int): Length of side of square
        position(tuple): Coordinate representation
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square class

        Args:
            size (int): Length of side of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Modifies the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Modifies the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Modify the position attribute"""
        if (
           type(value) is not tuple or len(value) != 2 or
           type(value[0]) is not int or type(value[1]) is not int or
           value[0] < 0 or value[1] < 0
           ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of a square

        Returns:
            int: Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints square of # chars """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print((" " * self.position[0]) + ('#' * self.size))
