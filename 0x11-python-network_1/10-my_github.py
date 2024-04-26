#!/usr/bin/python3
"""
script that takes your GitHub credentials (username
and password) and uses the GitHub API to display
your id
"""
import requests
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))

    try:
        json_response = r.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if json_response.get("id"):
        print(json_response.get("id"))
    else:
        print("None")
