#!/bin/bash

#Figure out better way to run commands

sudo apt-get update
sudo add-apt-repository ppa:pypy/ppa -y
sudo apt-get update
sleep 2.5
sudo apt install pypy3 -y
sleep 2.5
wget https://bootstrap.pypa.io/get-pip.py && pypy3 get-pip.py