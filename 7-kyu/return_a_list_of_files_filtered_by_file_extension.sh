#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please provide a file extension as an argument"
    exit 1
fi

extension="$1"
extension="${extension#.}"
ls -1 *.${extension} 2>/dev/null || true
