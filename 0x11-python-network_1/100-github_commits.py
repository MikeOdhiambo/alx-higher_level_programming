#!/usr/bin/python3
"""Takes GitHub credentials and displays id"""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.\
            format(owner, repo)

    req = requests.get(url)
    if req.status_code == 200:
        req_json = req.json()
        for i in range(10):
            sha_code = req_json[i]['sha']
            user = req_json[i]['commit']['author']['name']
            print("{}: {}".format(sha_code, user))
