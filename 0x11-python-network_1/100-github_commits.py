#!/usr/bin/python3
""" Script that takes 2 arguments with GitHub API
"""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                         format(sys.argv[2], sys.argv[1]))
        response_json = r.json()
        # print(response_json[0]['commit']['author']['name'])
        for commit in range(10):
            print("{}: {}".format(response_json[commit].get('sha'),
                                  response_json[commit].get('commit').
                                  get('author').get('name')))
    except:
        print("", end="")
