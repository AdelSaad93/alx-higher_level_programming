#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in the dictionary.

    Args:
        a_dictionary: The input dictionary.

    Returns:
        The key with the biggest integer value, or None if the dictionary is empty.
    """
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
