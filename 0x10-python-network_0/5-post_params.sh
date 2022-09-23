#!/bin/bash
# Sends a post request to URL with given headers
curl -sX "POST" -F "email=test@gmail.com" -F "subject=I will always be here for PLD" $1
