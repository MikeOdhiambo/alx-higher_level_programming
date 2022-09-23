#!/bin/bash
# Sends a GET request to URL and sets header variable
curl -sIX "GET" -H "X-School-User-Id: 98" $1
