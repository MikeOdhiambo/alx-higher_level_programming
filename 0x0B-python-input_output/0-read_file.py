#!/usr/bin/python3
""" A read_file module """


def read_file(filename=""):
    """ Reads contents of a file, printing to stdout """
    with open(filename, 'r', encoding="utf-8") as f:
        full_text = f.read()

    print(full_text)
