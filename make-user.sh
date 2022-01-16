#!/bin/bash

if id "$1" ; then
    echo "User already exists, skipping creating user..."
else
    adduser --disabled-password --gecos "" $1
fi