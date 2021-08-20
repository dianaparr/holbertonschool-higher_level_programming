#!/usr/bin/python3
""" Module that sends request to the URL and displays
    the value of the one variable found in the header of
    the response. """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
