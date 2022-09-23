#!/usr/bin/python3
"""
Sends POST request with email parameter and displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import parse, request

    url = argv[1]
    val = {'email': argv[2]}
    data = parse.urlencode(val)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        full_resp = resp.read()
        print(full_resp.decode('utf-8'))
