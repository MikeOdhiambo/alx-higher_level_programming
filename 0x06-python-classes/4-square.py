#!/usr/bin/python3
""" A simple module with the Square class """


class Square:
    """
    A Square class definition

    Attributes:
        size(int): Length of side of square
        position(object: tuple): A tuple representing coordinates
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square class

        Args:
            size (int): Length of side of square
        """
        self.__size = size
        self._position = position

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

    @property
    def position(self):
        """ Get position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set the coordinate to value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
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
        """ Prints the square in # chars"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)

    def my_print(self):
        """ Print the square in # chars """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
