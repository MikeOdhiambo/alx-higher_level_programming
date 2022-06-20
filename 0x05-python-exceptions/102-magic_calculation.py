#!/usr/bin/python3
def magic_calculation(x, y):
    result = 0
    for i in range(1, 3):
        try:
            if i > x:
                raise Exception('Too Far')
            else:
                result += x ** y / i
        except EXCEPTION:
            result = y + x
            break
    return result
