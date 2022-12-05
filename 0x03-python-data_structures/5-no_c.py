#!/usr/bin/python3

# Author: Samuel Mukosa Chibwe
# File: 5-no_c.py

def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
