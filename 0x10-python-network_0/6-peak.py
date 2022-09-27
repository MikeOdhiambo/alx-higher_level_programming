#!/usr/bin/python3
"""peak.py - Calculates the peak in a list of numbers"""


def find_peak(list_of_integers):
    """Returns the peak in a given list"""
    len_lst = len(list_of_integers)

    if len_lst == 0:
        return None
    elif len_lst == 1:
        return list_of_integers[0]
    elif len_lst == 2:
        return max(list_of_integers)
    else:
        md = len_lst // 2
        peak = list_of_integers[md]
        lhs = list_of_integers[md - 1]
        rhs = list_of_integers[md + 1]

        if peak > lhs and peak > rhs:
            return peak
        elif peak <= lhs:
            return find_peak(list_of_integers[:md])
        else:
            return find_peak(list_of_integers[md:])
