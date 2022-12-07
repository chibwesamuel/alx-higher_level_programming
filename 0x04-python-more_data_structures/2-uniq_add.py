#!/usr/bin/python3
#Author: Samuel Mukosa Chibwe
#File: 2-uniq_add.py

def uniq_add(my_list=[]):
    result = 0
    for x in set(my_list):
        result += x
    return (result)
