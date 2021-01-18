import ast
import sys
from modules.run import run
from modules.repository import orm
import os
import json
dirname = os.path.dirname(__file__)

input_path = os.path.join(dirname, 'data/input/{file}')
output_path = os.path.join(dirname, 'data/output/{file}')

params_dict = dict(job_name='pre_proc', input_path=input_path,
              output_path=output_path)

params = json.dumps(params_dict)

if __name__ == '__main__':

    parameters = ast.literal_eval(params)
    run(parameters)
