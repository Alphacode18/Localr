#!/bin/bash

echo "Installing package management utilities for PyPy3..."
sudo snap install pypy3 --classic
echo "done"

echo "Installing necessary packages for benchmarks..."
pypy3 -m ensurepip
pypy3 -m pip install jinja2
pypy3 -m pip install igraph
pypy3 -m pip install minio
echo "done"

echo "Running all benchmarks..."
for benchmark in /vagrant/benchmarks/*
do
    for run in {1..500}
    do
        pypy3 ${benchmark}/init.py $run
    done
done
