#!/bin/bash
#This script takes in a URL as an argument, sends a GET request to the URL & displays the body of the response
curl -sX GET "$1" -H "X-School-User-Id: 98"
