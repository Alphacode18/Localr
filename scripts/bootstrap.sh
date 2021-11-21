#!/bin/bash

echo "Updating all software packages..."
sudo apt-get update -qq
echo "done"

echo "Installing the PyPy3 runtime..."
sudo add-apt-repository ppa:pypy/ppa
echo
sudo apt-get update -qq
sudo apt install pypy3 -y -qq
echo "done"

echo "Installing package management utilities for PyPy3..."
wget -q https://bootstrap.pypa.io/get-pip.py
pypy3 get-pip.py
echo "done"
