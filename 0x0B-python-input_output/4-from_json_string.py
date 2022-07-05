#!/usr/bin/python3
""" This module contains the function from_json_string """
import json


def from_json_string(my_str):
    """ Returns an object from a JSON string """
    return json.loads(my_str)
