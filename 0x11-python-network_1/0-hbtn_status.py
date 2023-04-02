#!/usr/bin/python3
""" Fetches a given url"""
import urllib


if __name__ == "__main__":
    """ Load the request and format the response. """
    with urllib.requests.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print("body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
