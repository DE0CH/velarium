#!/bin/bash

if id "$1"; then
    echo "User already exists, skipping creating user..."
else
    adduser --disabled-password --gecos "" $1
fi

su -c "mdkri -p ~/.ssh && curl https://github.com/$2.keys > ~/.ssh/authorized_keys" - $1

