#!/usr/bin/python3
"""Sends request to a URL and displays error code if >= 400"""


if __name__ == "__main__":
    import requests
    from sys import argv

    req = argv[1]
    resp = requests.get(req)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
