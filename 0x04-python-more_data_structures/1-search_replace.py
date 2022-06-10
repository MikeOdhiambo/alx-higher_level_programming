#!/usr/bin/python3
def search_replace(my_list, search, replace):
    func = lambda x: x if (x != search) else replace
    rep_list = list(map(func, my_list))
    return rep_list
