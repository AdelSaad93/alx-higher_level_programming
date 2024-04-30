#!/usr/bin/python3
"""Defines a function to check if an object is an instance of a class that inherited ."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from a specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
