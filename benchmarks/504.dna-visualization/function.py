import datetime, io, json
from squiggle import transform

def handler(iteration, event):
    input_bucket = event.get('bucket').get('input')
    output_bucket = event.get('bucket').get('output')
    key = event.get('object').get('key')
    store = event.get('object').get('store')
    download_path = '/tmp/{}'.format(key)

    download_begin = datetime.datetime.now()
    store.download(input_bucket, key, download_path)
    download_stop = datetime.datetime.now()
    data = open(download_path, "r").read()

    process_begin = datetime.datetime.now()
    result = transform(data)
    process_end = datetime.datetime.now()

    upload_begin = datetime.datetime.now()
    buf = io.BytesIO(json.dumps(result).encode())
    buf.seek(0)
    key_name = store.upload_stream(output_bucket, key, buf)
    upload_stop = datetime.datetime.now()
    buf.close()

    download_time = (download_stop - download_begin) / datetime.timedelta(microseconds=1)
    process_time = (process_end - process_begin) / datetime.timedelta(microseconds=1)

    with open(f'504.dna-visualization_result.csv', 'a') as f:
      f.writelines(f"{iteration},{process_time}\n")

    return {
            'result': {
                'bucket': output_bucket,
                'key': key_name
            },
            'measurement': {
                'download_time': download_time,
                'compute_time': process_time
            }
    }
