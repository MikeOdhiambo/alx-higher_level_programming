#!/usr/bin/python3
"""Sends a request to URL and handles HTTP errors"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request
    from urllib.error import HTTPError

    url = argv[1]
    try:
        with request.urlopen(url) as req:
            full_resp = req.read()
            print(full_resp.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
