#!/bin/bash

echo "Updating all software packages..."
sudo apt-get update -qq
echo "done"

echo "Installing the snap package manager..."
sudo apt install snapd -y
echo "done"