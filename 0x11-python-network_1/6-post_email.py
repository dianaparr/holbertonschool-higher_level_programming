#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a parameter """
import requests
import sys

if __name__ == "__main__":
    parameter = {'email': sys.argv[2]}
    # pass a dictionary to the data argument, automatically be encoded
    r = requests.post(sys.argv[1], data=parameter)
    print(r.text)
