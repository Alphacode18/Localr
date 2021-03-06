from datetime import date, datetime                                                   
import random
from os import path
from time import time                                                           

from jinja2 import Template

SCRIPT_DIR = path.abspath(path.join(path.dirname(__file__)))

def handler(event, iteration, run, seed):

    name = event.get('username')
    size = event.get('random_len')
    start = datetime.now()
    cur_time = datetime.now()
    random.seed(seed)
    random_numbers = random.sample(range(0, 1000000), size)
    template = Template( open(path.join(SCRIPT_DIR, 'templates', 'template.html'), 'r').read())
    html = template.render(username = name, cur_time = cur_time, random_numbers = random_numbers)
    end = datetime.now()
    # dump stats 
    with open(f'/vagrant/results/runs/110.dynamic-html/110.dynamic-html_result_{run}.csv', 'a') as f:
      f.writelines(f"{iteration},{(end - start).microseconds}\n")
    return {'result': html}

