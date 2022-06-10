#!/usr/bin/python3
def roman_to_int(roman_string):
    dec = 0
    conv_tab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i > 0 and conv_tab[roman_string[i]] > conv_tab[roman_string[i - 1]]:
            dec += conv_tab[roman_string[i]] - 2 * \
                conv_tab[roman_string[i - 1]]
        else:
            dec += conv_tab[roman_string[i]]
    return dec
