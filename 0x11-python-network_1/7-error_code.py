#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    """Print error code and value of the HTTP status code"""
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >=  400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)