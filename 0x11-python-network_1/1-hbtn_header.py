#!/usr/bin/python3
"""Sends a request to URL and displays value of X-Request-Id"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request

    with request.urlopen("{}".format(argv[1])) as req:
        print(req.headers['X-Request-Id'])
