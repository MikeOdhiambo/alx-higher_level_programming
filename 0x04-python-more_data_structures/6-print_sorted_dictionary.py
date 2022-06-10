#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    srted = sorted(a_dictionary)
    for itm in srted:
        print("{}: {}".format(itm, a_dictionary[itm]))
