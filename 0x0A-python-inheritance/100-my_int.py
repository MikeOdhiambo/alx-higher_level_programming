#!/usr/bin/python3
""" This module extends int class """


class MyInt(int):
    """
    Inherits from int, reversing the behavior of != and ==
    """

    def __eq__(self, value):
        """ Return not equal instead of equal """
        return super().__ne__(value)

    def __ne__(self, value):
        """ Return equal instead of not equal """
        return super().__eq__(value)
