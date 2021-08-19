#!/bin/bash
# Script that show the size of the body of the response: Parameter $1 0.0.0.0:5000
curl -s -I "$1" | grep Content-Length | cut -d' ' -f2
