#!/bin/bash

#vagrant up

for benchmark in 110.dynamic-html 501.graph-pagerank 502.graph-mst 503.graph-bfs
do
    echo $benchmark
    python3 ../python/processor.py $benchmark
    python3 ../python/grapher.py $benchmark
done