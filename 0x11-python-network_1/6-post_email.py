#!/usr/bin/python3
"""Sends POST request to URL and displays the response body"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    req = requests.post(url, data={'email': argv[2]})
    print(req.text)
