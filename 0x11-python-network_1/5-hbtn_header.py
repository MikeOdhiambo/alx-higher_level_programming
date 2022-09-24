#!/usr/bin/python3
"""Sends request to URL and displays value of X-Request-Id"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
