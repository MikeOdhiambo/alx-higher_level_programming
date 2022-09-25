#!/bin/bash
# Sends a JSON POST request and displays the body of the response
curl -s -X POST --data "@$2" $1 
