#!/bin/bash
# Scripts displays only the status code of the response
curl -s -I -o -L -w "%{http_code}" "$1"
