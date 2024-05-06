#!/usr/bin/python3
"""Defines a function to save an object to a JSON file."""


def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file.

    Args:
        my_obj (object): The object to be saved.
        filename (str): The name of the file to save the object to.
    """
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
