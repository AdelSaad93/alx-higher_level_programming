#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list_and_save():
    """
    Adds all command line arguments to a Python list and saves them to a file.
    The list is saved as a JSON representation in a file named add_item.json.
    If the file doesn’t exist, it is created.
    """
    filename = "add_item.json"

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_items_to_list_and_save()
