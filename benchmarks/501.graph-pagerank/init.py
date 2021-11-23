import sys
from function import handler

def generate_input():
    input_config = {'size': 10} 
    return input_config

for iteration in range(0, 1000):
  input_conf = generate_input()
  handler(input_conf, iteration, sys.argv[1])