#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses
the GitHub API to display your id

Usage: ./10-my_github.py smchibwe atoi
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("http://api.github.com/uer", auth=auth)
    print(r.json().get("id"))
