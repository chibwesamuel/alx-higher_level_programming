#!/usr/bin/python3

# Author: Samuel Mukosa Chibwe
# File: 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """function that prints all integers of a list"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
