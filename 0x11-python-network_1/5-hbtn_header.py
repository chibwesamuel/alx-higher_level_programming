#!/usr/bin/python3
"""
Displays the value of X-Request-Id of URL in response to request

Usage: ./5-hbtn_header.py https://alx-intranet.hbtn.io
"""
import urllib.requests
import sys

if __name__ == "__main__":
    """Takes URL request and returns X-Request-Id"""
    url = sys.argv[]

    r = requests.get(url)
    print(r.headers.get("X-Requests-Id"))
