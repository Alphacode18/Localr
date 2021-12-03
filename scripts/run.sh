#!/bin/bash

echo "Installing package management utilities for PyPy3..."
sudo snap install pypy3 --classic
sudo apt update
sudo apt install ffmpeg -y
echo "done"

echo "Installing necessary packages for benchmarks..."
pypy3 -m ensurepip
pypy3 -m pip install jinja2
pypy3 -m pip install igraph
pypy3 -m pip install minio
pypy3 -m pip install urllib3
pypy3 -m pip install Pillow
pypy3 -m pip install squiggle
echo "done"

echo "Installing docker..."
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
echo "done"

echo "Pulling Minio image"
sudo docker pull minio/minio
echo "done"

echo "Starting Minio server"
sudo docker run -d -p 9000:9000 -p 9001:9001 minio/minio server /data --console-address ":9001"
echo "done"

echo "Ensuring all services are started and running..."
sleep 1m
echo "done"

echo "Running all benchmarks..."
for benchmark_path in /vagrant/benchmarks/*
do
    benchmark=$(echo $benchmark_path | cut -d "/" -f 4)
    if [[ "$benchmark" != *"data"* && "$benchmark" != *"dna"* ]]; then
        for run in {1..20}
        do
            pypy3 ${benchmark_path}/init.py $run
        done
    fi
done
