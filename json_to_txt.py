#!/bin/python3

"""Convert json to txt """

import os
import json

PATH = os.getcwd()

with open(f"{PATH}analysis_parameters.json", "r") as analysis_parameters:
    data = json.load(analysis_parameters)

with open(f"{PATH}analysis_parameters.txt", "w") as analysis_parameters:
    for line in data.values():
        analysis_parameters.write(str(line) + '\n')
