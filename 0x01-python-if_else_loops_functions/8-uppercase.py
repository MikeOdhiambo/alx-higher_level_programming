#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for char in str:
        if ord(char) < 97:
            upper += char
        else:
            upper += chr(ord(char) - 32)
    return upper
