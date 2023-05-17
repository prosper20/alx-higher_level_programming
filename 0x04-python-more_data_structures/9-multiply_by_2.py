#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dir = a_dictionary.copy()
    keys_list = list(my_dir.keys())

    for i in keys_list:
        my_dir[i] *= 2

    return (my_dir)
