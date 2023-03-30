#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI "$0" | grep "Allow" | cut -d " " -f 2-
