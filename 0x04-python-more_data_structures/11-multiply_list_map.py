#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Returns a new list with each value multiplied by a number using map."""
    return list(map(lambda x: x * number, my_list))