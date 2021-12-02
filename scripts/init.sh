#!/bin/bash

# vagrant up

for benchmark in 110.dynamic-html 501.graph-pagerank 502.graph-mst 503.graph-bfs
do
    python3 ../utilities/processor.py $benchmark
    #python3 ../utilities/grapher.py $benchmark
done
