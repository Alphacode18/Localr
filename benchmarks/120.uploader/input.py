url_generators = {
    # source: mlperf fake_imagenet.sh. 230 kB
    'test' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Jammlich_crop.jpg/800px-Jammlich_crop.jpg',
    # video: HPX source code, 6.7 MB
    'small': 'https://github.com/STEllAR-GROUP/hpx/archive/1.4.0.zip',
    # resnet model from pytorch. 98M
    'large':  'https://download.pytorch.org/models/resnet50-19c8e357.pth'
}

def buckets_count():
    return (0, 1)

def generate_input(size, output_buckets):
    input_config = {'object': {}, 'bucket': {}}
    input_config['object']['url'] = url_generators[size]
    input_config['bucket']['output'] = output_buckets[0]
    return input_config
