import os
from storage import storage
from input import generate_input
from function import handler

store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

client.make_bucket("311.compression-in")
client.make_bucket("311.compression-out")

def cleanup(bucket, object_name):
  client.remove_object(bucket, object_name)

for iteration in range(0, 1000):
  input_conf = generate_input(data_dir=os.path.join(ROOT_DIR, "benchmarks", "data", "311.compression"),
                              input_buckets=["311.compression-in"],
                              output_buckets=["311.compression-out"],
                              upload_func=store.upload)
  input_conf['object']['store'] = store
  handler(iteration, input_conf)
  cleanup("311.compression-in", input_conf['object']['key'])
  cleanup("311.compression-out", f"processed-{input_conf['object']['key']}")