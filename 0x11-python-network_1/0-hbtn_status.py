#!/usr/bin/python3
""" Module that fetches a URL """
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as resp:
        page = resp.read()
        print("Body response:\n\
        - type: {}\n\
        - content: {}\n\
        - utf8 content: {}".format(
            type(page), page, page.decode('utf-8')))
