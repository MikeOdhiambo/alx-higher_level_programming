#!/usr/bin/python3
""" This module contains the function append_after """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to file after specific string
        Args:
            filename('str'): name of file
            search_string('str): string to find in line
            new_string('str'): string to add
    """
    with open(filename) as f:
        lines = f.readlines()

    with open(filename, "w") as fw:
        l = ""
        for line in lines:
            l += line
            if search_string in line:
                l += new_string
        fw.write(l)
