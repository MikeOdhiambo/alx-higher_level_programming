#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep_list = list(map(lambda x: x if (x != search) else replace, my_list))
    return rep_list