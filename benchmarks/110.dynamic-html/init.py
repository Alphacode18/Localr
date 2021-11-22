from function import handler

def generate_input():
    input_config = {'username': 'testname'} 
    input_config['random_len'] = 10
    return input_config

for i in range(0, 1000):
  input_conf = generate_input()
  handler(input_conf, i)