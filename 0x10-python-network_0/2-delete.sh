#!/bin/bash
# Sends a DELETE request to the URL passed Parameters $1 0.0.0.0:5000
curl -s -X DELETE "$1"
