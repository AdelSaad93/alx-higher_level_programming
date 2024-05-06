#!/usr/bin/python3
"""Defines a function to return an object represented by a JSON string."""


def from_json_string(my_str):
    """Return the object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        object: The object represented by the JSON string.
    """
    import json
    return json.loads(my_str)
