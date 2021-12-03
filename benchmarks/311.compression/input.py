import glob, os

def buckets_count():
    return (1, 1)


def upload_files(data_root, data_dir, upload_func, input_bucket):

    for root, dirs, files in os.walk(data_dir):
        prefix = os.path.relpath(root, data_root)
        for file in files:
            file_name = prefix + '/' + file
            filepath = os.path.join(root, file)
            upload_func(input_bucket, file_name, filepath)

def generate_input(data_dir, input_buckets, output_buckets, upload_func):

    datasets = []
    for dir in os.listdir(data_dir):
        datasets.append(dir)
        upload_files(data_dir, os.path.join(data_dir, dir), upload_func, input_buckets[0])

    input_config = {'object': {}, 'bucket': {}}
    input_config['object']['key'] = datasets[0]
    input_config['bucket']['input'] = input_buckets[0]
    input_config['bucket']['output'] = output_buckets[0]
    return input_config
