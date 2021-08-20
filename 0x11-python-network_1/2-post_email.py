#!/usr/bin/python3
""" Module that sends a POST request and
    displays the body of the response (decoded in utf-8) """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    # encoded to bytes before it is sent to urlopen as data
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read().decode('utf-8')
        print(page)
