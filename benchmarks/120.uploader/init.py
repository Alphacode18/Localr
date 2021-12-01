import os
from storage import storage
from input import generate_input
from function import handler

store = storage()
client = store.client
ROOT_DIR = os.path.abspath("../..")

client.make_bucket("120.uploader")

def cleanup(bucket, object_name):
  client.remove_object(bucket, object_name)

for iteration in range(0, 5000):
  input_conf = generate_input(size="test", output_buckets=["120.uploader"])
  input_conf['object']['store'] = store
  handler(iteration, input_conf)
  cleanup("120.uploader", "800px-Jammlich_crop.jpg")