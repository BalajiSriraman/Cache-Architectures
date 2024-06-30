#!/bin/bash

# Check if a package name was provided
if [ $# -eq 0 ]; then
    echo "Please provide a package name."
    exit 1
fi

# Install the package
uv pip install "$1"

# Update requirements.txt
pip freeze > requirements.txt

echo "Package $1 installed and requirements.txt updated."
