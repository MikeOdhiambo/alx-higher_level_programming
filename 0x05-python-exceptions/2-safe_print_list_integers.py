#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    lst_len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            lst_len += 1
        except (ValueError, TypeError):
            lst_len += 0
    print("")
    return (lst_len)
