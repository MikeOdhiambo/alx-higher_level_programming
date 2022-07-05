#!/usr/bin/python3
""" This module contains the write_file function """


def write_file(filename="", text=""):
    """ Writes contents to a file, overwriting existing ones """
    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)

    return chars
