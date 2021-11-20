#!/bin/bash
FILE=Vagrantfile
IMAGE=ubuntu/trusty64
if [ ! -f "$FILE" ]; then
  vagrant init $IMAGE
fi
vagrant up
vagrant ssh