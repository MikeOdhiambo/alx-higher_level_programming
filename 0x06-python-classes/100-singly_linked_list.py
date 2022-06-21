#!/usr/bin/python3
""" A module for a Single linked list and a Node """


class Node:
    """
    Node of a singly linked list.

    Args:
        data(int): Data item on node
        next_node(obj): Next node on list
    """

    def __init__(self, data, next_node=None):
        """Initialize a node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data from node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Modify data on node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list """

    def __init__(self):
        """Initialize the linked list."""
        self.head = None

    def __str__(self):
        """Print list as a string object"""
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted linked list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
