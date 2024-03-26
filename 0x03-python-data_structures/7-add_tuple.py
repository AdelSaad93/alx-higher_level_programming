#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a += (0, )
    if len(tuple_b) < 2:
        tuple_b += (0, )

    # If a tuple is bigger than 2, use only the first 2 integers
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result


if __name__ == "__main__":
    tuple_a = ()
    tuple_b = (1, 2)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)
