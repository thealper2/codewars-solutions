#!/bin/bash

latest_file=$(ls -t | head -n 1)
if [ -z "$latest_file" ]; then
    echo "No files found in the current directory."
    exit 1
fi

echo "$latest_file"
