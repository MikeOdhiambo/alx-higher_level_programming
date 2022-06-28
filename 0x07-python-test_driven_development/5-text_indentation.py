#!/usr/bin/python3
""" This module prints a string with two new lines """


def text_indentation(text):
    """
    Args:
        text: string to parse
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n").replace("? ", "?\n\n")\
        .replace(": ", ":\n\n")
    sub_str = text.splitlines(keepends=True)
    ret = ""
    for words in sub_str:
        ret += words.strip(" ")
    print(ret, end="")