#!/bin/bash
# Script with curl GET Request with custom HTTP header. Param $1 0.0.0.0:5000
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
