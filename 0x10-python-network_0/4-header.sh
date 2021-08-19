#!/bin/bash
# Script with curl GET Request with custom HTTP header. Param $1 0.0.0.0:5000
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
