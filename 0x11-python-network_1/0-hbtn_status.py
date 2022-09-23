#!/usr/bin/python3
"""hbtn_status.py- Fetches a URL and prints it in a formatted manner """


if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        cont = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(cont)))
        print("\t- content: {}".format(cont))
        print("\t- utf8 content: {}".format(cont.decode("utf-8")))
