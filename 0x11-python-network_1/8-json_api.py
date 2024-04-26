#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a
parameter.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    r = requests.post(url, data=data)

    try:
        json_response = r.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()

    if json_response:
        print("[{}] {}".format(
            json_response.get("id"), json_response.get(
                "name")))
    else:
        print("No result")
