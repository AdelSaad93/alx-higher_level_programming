#!/usr/bin/python3
"""Defines a function to load an object from a JSON file."""


def load_from_json_file(filename):
    """Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object loaded from the JSON file.
    """
    import json
    with open(filename, 'r') as file:
        return json.load(file)
