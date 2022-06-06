#!/usr/bin/python3
def first(sentence):
    if sentence:
        return sentence[0]
    return None


def multiple_returns(sentence):
    f_char = first(sentence)
    len_s = len(sentence)
    return (len_s, f_char)
