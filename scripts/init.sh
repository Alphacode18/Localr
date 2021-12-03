# #!/bin/bash

# PROJ_DIR=$(pwd)/..

# for benchmark_path in $PROJ_DIR/benchmarks/*
# do
#     benchmark=$(echo $benchmark_path | cut -d "/" -f 11)
#     if [[ "$benchmark" != *"data"* && "$benchmark" != *"dna"* ]]; then
#         mkdir -p $PROJ_DIR/results/runs/$benchmark
#     fi
# done

# vagrant up

for benchmark_path in $PROJ_DIR/results/runs/*
do
    benchmark=$(echo $benchmark_path | cut -d "/" -f 12)
    python3 $PROJ_DIR/utilities/processor.py $benchmark
    python3 $PROJ_DIR/utilities/grapher.py $benchmark
done
