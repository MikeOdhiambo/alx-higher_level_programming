#!/bin/bash
# Sends a request using curl and displays the status code of the response
curl -so /dev/null -w '%{http_code}' $1
