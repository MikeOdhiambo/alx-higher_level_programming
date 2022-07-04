#!/usr/bin/python3
""" MyList: Extends the list class """


class MyList(list):
    """ MyList class that extends the list class """

    def print_sorted(self):
        new_list = [i for i in self]
        new_list.sort()

        print(new_list)
