#!/usr/bin/python3
""" Module that sends request to the URL and displays
    the value of the one variable found in the header of
    the response. """
import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as resp:
        # use that request objects method
        header = resp.getheader('X-Request-Id')
        print(header)
