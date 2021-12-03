import glob, os

def buckets_count():
    return (1, 1)

def generate_input(data_dir, input_buckets, output_buckets, upload_func):
    for file in glob.glob(os.path.join(data_dir, '*.mp4')):
        img = os.path.relpath(file, data_dir)
        upload_func(input_buckets[0], img, file)
    input_config = {'object': {}, 'bucket': {}}
    input_config['object']['key'] = img
    input_config['object']['op'] = 'watermark'
    input_config['object']['duration'] = 1
    input_config['bucket']['input'] = input_buckets[0]
    input_config['bucket']['output'] = output_buckets[0]
    return input_config
