#!/usr/bin/python3
""" This module adds an item to a json list """
import json
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    args_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    args_list = []
for arg in sys.argv:
    if arg is sys.argv[0]:
        continue
    args_list.append(arg)

save_to_json_file(args_list, 'add_item.json')
