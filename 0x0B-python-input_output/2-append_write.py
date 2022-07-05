#!/usr/bin/python3
""" This module contains the function append_write """


def append_write(filename="", text=""):
    """ Adds text to a file object without overwriting """
    with open(filename, 'a', encoding="utf-8") as f:
        appended = f.write(text)

    return appended
