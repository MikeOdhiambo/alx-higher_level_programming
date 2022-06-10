#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tot = sum([num[0] * num[1] for num in my_list])
    return tot / sum([num[1] for num in my_list])
