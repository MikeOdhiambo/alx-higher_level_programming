#!/usr/bin/python3
"""Takes GitHub credentials and displays id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    username = argv[1]
    passwrd = argv[2]

    req = requests.get(url, auth=(username, passwrd))
    if req.status_code == 200:
        print(req.json()['id'])
    else:
        print("None")
