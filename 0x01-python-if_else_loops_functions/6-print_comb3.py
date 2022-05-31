#!/usr/bin/python3

for digt1 in range(0, 10):
    for digt2 in range(0, 10):
        if digt1 - digt2 >= 0:
            continue
        elif digt1 == 8 and digt2 == 9:
            print(f"{digt1}{digt2}", end="\n")
        else:
            print(f"{digt1}{digt2}", end=", ")
