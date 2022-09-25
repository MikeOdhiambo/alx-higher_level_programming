#!/bin/bash
# Sends a JSON POST request and displays the body of the response
curl -sX POST $1 -d @$2 
