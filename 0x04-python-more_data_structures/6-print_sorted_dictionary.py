#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    aList = list(a_dictionary.keys())
    aList.sort()
    for i in aList:
        print("{}: {}".format(i, a_dictionary.get(i)))
