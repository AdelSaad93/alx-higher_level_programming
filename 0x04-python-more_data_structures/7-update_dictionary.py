#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The input dictionary.
        key: The key to replace or add.
        value: The value to assign to the key.

    Returns:
        The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
