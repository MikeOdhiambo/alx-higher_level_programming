#!/usr/bin/env python3

def print_last_digit(number):
    if number < 0:
        last = (number * -1) % 10
    last = number % 10
    return last
