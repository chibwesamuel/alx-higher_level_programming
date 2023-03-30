#!/bin/bash
# ends a request to the URL and displays the size of the body of the response
curl -s -w | wc -c
