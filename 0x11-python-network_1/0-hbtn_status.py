#!/usr/bin/python3

if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        req = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(req)))
        print("\t- content: {}".format(req))
        print("\t- utf8 content: {}".format(req.decode("utf-8")))
