#!/usr/bin/python3
""" Module that takes in a letter and sends a POST request to url
    with the letter as a parameter """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        var = {'q': sys.argv[1]}
    else:
        var = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=var)
    try:
        response_json = r.json()
        if len(response_json) != 0:
            print("[{}] {}".format(response_json['id'], response_json['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
