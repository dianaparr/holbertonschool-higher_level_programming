#!/bin/bash
# Script that sends a JSON; -d"@"$2" -> the rest should be a file name to read the data from
curl -s -H "Content-Type: application/json" -X POST -d "@""$2" "$1"
