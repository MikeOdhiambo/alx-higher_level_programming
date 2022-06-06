#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if len_list == 0:
        return None
    else:
        max = my_list[0]
        for num in my_list:
            if num > max:
                max = num
    return max
