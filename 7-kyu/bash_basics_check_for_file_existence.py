#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Nothing to find"
    exit 0
fi

filename="$1"

if [ -f "$filename" ]; then
    echo "Found $filename"
else
    echo "Can't find $filename"
fi
