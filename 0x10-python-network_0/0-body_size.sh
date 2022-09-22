#!/bin/bash
# Displays the size of a URL response body
curl -sI $1 | grep 'Content-Length' | awk '{print $2}'
