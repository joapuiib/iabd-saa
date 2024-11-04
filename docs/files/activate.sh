#!/bin/bash

CREATED_VENV=0
if [ ! -d "~/.saa-venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv ~/.saa-venv
    CREATED_VENV=1
fi

echo "Activating virtual environment..."
source ~/.saa-venv/bin/activate

if [ $CREATED_VENV -eq 1 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi
