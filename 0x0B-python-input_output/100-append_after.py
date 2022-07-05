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
        new_line = ""
        for line in lines:
            new_line += line
            if search_string in line:
                new_line += new_string
        fw.write(new_line)
