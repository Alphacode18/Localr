import os
import sys
from storage import storage
from input import generate_input
from function import handler

store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

if (client.bucket_exists("220.video-processing-in") == False ):
  client.make_bucket("220.video-processing-in")

if (client.bucket_exists("220.video-processing-out") == False ):
  client.make_bucket("220.video-processing-out")

def cleanup(bucket, object_name):
  client.remove_object(bucket, object_name)

for iteration in range(0, 2500):
  input_conf = generate_input(data_dir="/vagrant/benchmarks/data/220.video-processing",
                              input_buckets=["220.video-processing-in"],
                              output_buckets=["220.video-processing-out"],
                              upload_func=store.upload)
  input_conf['object']['store'] = store
  handler(iteration, input_conf, sys.argv[1])
  cleanup("220.video-processing-in", input_conf['object']['key'])
  cleanup("220.video-processing-out", f"processed-{input_conf['object']['key']}")