#!/usr/bin/python3
"""Fetches a URL using requests"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(req)))
    print("\t- content: {}".format(req))
