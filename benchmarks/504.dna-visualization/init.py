import os
import sys
from storage import storage
from input import generate_input
from function import handler


store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

dup_guard = client.bucket_exists("504.dna-visualization-in")
if not dup_guard:
  client.make_bucket("504.dna-visualization-in")
dup_guard = client.bucket_exists("504.dna-visualization-out")
if not dup_guard:
  client.make_bucket("504.dna-visualization-out")

for iteration in range(0, 1):
  input_conf = generate_input(data_dir=os.path.join(ROOT_DIR, "benchmarks", "data", "504.dna-visualization"),
                              input_buckets=["504.dna-visualization-in"],
                              output_buckets=["504.dna-visualization-out"],
                              upload_func=store.upload)
  input_conf['object']['store'] = store
  handler(input_conf)
