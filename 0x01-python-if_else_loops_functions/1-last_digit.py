#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dig = ((number * -1) % 10) * -1
else:
    last_dig = number % 10
if last_dig == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last_dig > 0 and last_dig < 6:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last_dig > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
