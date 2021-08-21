#!/usr/bin/python3
""" Module that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id"""
import requests
import requests.auth
import sys

if __name__ == "__main__":
    try:
        r = requests.get('https://api.github.com/user',
                         auth=(sys.argv[1], sys.argv[2]))
        response_json = r.json()
        print(response_json['id'])
    except:
        print("None")
