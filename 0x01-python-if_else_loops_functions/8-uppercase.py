#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for char in str:
        if ord(char) < 97:
            upper += char
        else:
            upper += chr(ord(char) - 32)
    print("{s}".format(upper), end="\n")
