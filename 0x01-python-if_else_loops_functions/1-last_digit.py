#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lst = ((number * -1) % 10) * -1
else:
    lst = number % 10
if lst == 0:
    print("Last digit of {} is {} and is 0".format(number, lst))
elif lst != 0 and lst < 6:
    print("Last digit of {0} is {1} and is less\
             than 6 and not 0").format(number, lst)
elif lst > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lst))
