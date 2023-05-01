#!/usr/bin/python3
"""Write a function that writes an Object
 to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Write and object using JSON representation
    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, mode="w", encoding="utf-8") as My_File:
        My_File.write(json.dumps(my_obj))
        