#!/bin/bash
# Displays the size of a URL response body
curl -sI $1 | grep 'content-length' | awk '{print $2}'
