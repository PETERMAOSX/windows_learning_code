import scipy.io
import pandas as pd
import xarray as xr
import numpy as np
from pprint import pprint
from functools import reduce
import re
from matplotlib import pyplot as plt
f = open("./data/64-channels.loc", "r")
lines = re.split('\n', f.read())
electrodes = []
for line in lines:
    electrodes.append(list(filter(lambda text: len(text) > 0, re.split('\s', line))))
electrodes = list(filter(lambda l: len(l) > 0, electrodes))
elec_to_elec_id_map = {}
elec_id_to_elec_map = {}
for i in range(len(electrodes)):
    elec_to_elec_id_map[electrodes[i][3]] = int(electrodes[i][0])
    elec_id_to_elec_map[int(electrodes[i][0])] = electrodes[i][3]
print(elec_id_to_elec_map)