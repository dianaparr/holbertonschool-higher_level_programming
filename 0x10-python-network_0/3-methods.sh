#!/bin/bash
# Script that takes in a URL and displays all HTTP methods. Param $1 0.0.0.0:5000
curl -s -I "$1" | grep Allow | cut -d' ' -f2-
