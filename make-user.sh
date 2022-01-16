#!/bin/bash

if id "$1" &>/dev/null; then
    echo "User already exists, skipping creating user..."
else
    adduser --disabled-password --gecos "" $1
fi