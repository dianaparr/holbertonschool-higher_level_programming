#!/usr/bin/python3
""" Module that fetches a URL - Import the Requests module """
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    # The text encoding guessed by Requests is used when
    # you access r.text
    print("Body response\
:\n\t- type: {}\n\t- content\
: {}".format(type(r.text), r.text))
