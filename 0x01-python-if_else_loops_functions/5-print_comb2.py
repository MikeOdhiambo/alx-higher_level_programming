#!/usr/bin/python3

for i in range(0, 100):
    if i == 99:
        print("{d}".format(i), end="\n")
    else:
        print("{d:02}".format(i), end=", ")
