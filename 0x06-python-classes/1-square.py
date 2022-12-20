#!/usr/bin/python3
#File: 1-square.py
#Auth: Samuel Chibwe
"""defines a square by: (based on 0-square.py)."""

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
