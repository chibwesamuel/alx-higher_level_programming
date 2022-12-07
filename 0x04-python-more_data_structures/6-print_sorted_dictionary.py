#!/usr/bin/python3
# Autjor: Samuel Mukosa Chibwe
# File: 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys."""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
