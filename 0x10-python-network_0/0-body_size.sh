#!/bin/bash
# Script that show the size of the body of the response
# Parameter $1 0.0.0.0:5000
curl -sI "$1" | grep Content-Length | cut -d' ' -f 2
