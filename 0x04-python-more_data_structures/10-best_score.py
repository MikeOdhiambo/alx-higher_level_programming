#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        for k, v in a_dictionary.items():
            if v == max(a_dictionary.values()):
                return k
