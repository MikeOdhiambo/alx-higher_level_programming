#!/bin/bash
# Sends a JSON POST request and displays the body of the response
curl -s --data "@$2" $1 
