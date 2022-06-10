#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for itm in list(a_dictionary):
        if a_dictionary[itm] == value:
            a_dictionary.pop(itm)
    return a_dictionary
