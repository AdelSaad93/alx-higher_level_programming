#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: The list of integers.

    Returns:
        The sum of all unique integers in the list.
    """
    unique_numbers = set(my_list)
    return sum(unique_numbers)
