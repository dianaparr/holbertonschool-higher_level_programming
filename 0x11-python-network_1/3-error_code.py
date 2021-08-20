#!/usr/bin/python3
""" Module that manage urllib.error.HTTPError exceptions and
    print error code - HTTP status code """
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            res = resp.read().decode('utf-8')
            print(res)
    except urllib.error.URLError as error:
        # The urllib.error module defines the exception classes
        # for exceptions raised by urllib.request
        print("Error code: {}".format(error.code))
