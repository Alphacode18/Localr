from minio import Minio
from minio.error import S3Error

from function import handler

client = Minio("localhost:9000", access_key="minioadmin", secret_key="minioadmin", secure=False)

def buckets_count():
    return (0, 1)

def generate_input():
    bucket_found = client.bucket_exists("120.uploader")
    if not bucket_found:
        client.make_bucket("120.uploader")
    input_config = {'object': {}, 'bucket': {}}
    input_config['object']['url'] = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Jammlich_crop.jpg/800px-Jammlich_crop.jpg'
    input_config['bucket']['output'] = '120.uploader'
    input_config['object']['client'] = client
    return input_config

for iteration in range(0, 1000):
  input_conf = generate_input()
  handler(input_conf, iteration)
