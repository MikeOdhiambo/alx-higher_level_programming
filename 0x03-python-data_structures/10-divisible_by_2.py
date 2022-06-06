#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_2 = []
    for num in my_list:
        div = bool(num % 2 == 0)
        list_2.append(div)
    return list_2
