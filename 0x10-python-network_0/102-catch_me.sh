#!/bin/bash
# Script that makes a request that causes the server to respond with a message
curl -sI -X PUT -H "Host:" 00.0.0:5000/catch_me
