import os
import sys
from storage import storage
from input import generate_input
from function import handler

store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

if (client.bucket_exists("210.thumbnailer-in") == False ):
  client.make_bucket("210.thumbnailer-in")

if (client.bucket_exists("210.thumbnailer-out") == False ):
  client.make_bucket("210.thumbnailer-out")

def cleanup(bucket, object_name):
  client.remove_object(bucket, object_name)

for iteration in range(0, 10):
  input_conf = generate_input(data_dir=os.path.join(ROOT_DIR, "benchmarks", "data", "210.thumbnailer"),
                              input_buckets=["210.thumbnailer-in"],
                              output_buckets=["210.thumbnailer-out"],
                              upload_func=store.upload)
  input_conf['object']['store'] = store
  handler(iteration, input_conf, sys.argv[1])