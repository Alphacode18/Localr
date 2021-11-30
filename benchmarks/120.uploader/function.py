import datetime
import os
import uuid

import urllib.request


def handler(event, iteration):
  
    output_bucket = event.get('bucket').get('output')
    url = event.get('object').get('url')
    client = event.get('object').get('client')
    name = os.path.basename(url)
    download_path = '/tmp/{}'.format(name)

    process_begin = datetime.datetime.now()
    urllib.request.urlretrieve(url, filename=download_path)
    size = os.path.getsize(download_path)
    process_end = datetime.datetime.now()

    upload_begin = datetime.datetime.now()
    key_name = client.fput_object(output_bucket, name, download_path)
    upload_end = datetime.datetime.now()

    process_time = (process_end - process_begin) / datetime.timedelta(microseconds=1)
    upload_time = (upload_end - upload_begin) / datetime.timedelta(microseconds=1)
    with open(f'120.uploader_result.csv', 'a') as f:
      f.writelines(f"{iteration},{(process_time)}\n")
    return {
            'result': {
                'bucket': output_bucket,
                'url': url,
                'key': key_name
            },
            'measurement': {
                'download_time': 0,
                'download_size': 0,
                'upload_time': upload_time,
                'upload_size': size,
                'compute_time': process_time
            }
    }
