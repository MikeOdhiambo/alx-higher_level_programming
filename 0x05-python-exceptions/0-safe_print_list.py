#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_len = 1
    for list_len in range((x + 1)):
        try:
            print(my_list[list_len], end="")
        except IndexError:
            break

    print("")
    return list_len
