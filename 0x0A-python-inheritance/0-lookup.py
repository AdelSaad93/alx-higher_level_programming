#!/usr/bin/python3
def lookup(obj):
    """
    Return a list of an object's available attributes.

    Args:
        obj (object): The object whose attributes are to be looked up.

    Returns:
        list: A list containing the names of the available attributes of the object.
    """
    return dir(obj)
