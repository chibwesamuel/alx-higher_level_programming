#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    """Disply letter as parameter for requests"""
    letter = "" if len(sys.argv) == 1
    else:
        letter = q
    r = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("Not a valid JSON")
