#!/usr/bin/python3

def remove_char_at(str, n):
    newStr = ""
    pos = 0
    for char in str:
        if pos != n:
            newStr += str[pos]
        pos++
    return newStr
