#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    del_list = my_list[:]
    del del_list[idx]
    return del_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list[:], idx)
    print(new_list)
    print(my_list)
