#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
curl -s "$1" | wc -c
