#!/usr/bin/python3
"""Takes in a letter, sends a POST request and displays search results"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    req = requests.post(url, data={'q': q})
    try:
        dct = req.json()
        if dct == {}:
            print('No result')
        else:
            print("[{}] {}".format(dct.get('id'), dct.get('name')))
    except ValueError:
        print('Not a valid JSON')
