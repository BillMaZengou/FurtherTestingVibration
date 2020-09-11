import glob
from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

table_dict = dict()
amplitude = dict()
def magnitude(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)

for file in glob.glob("resonance/*"):
    frequency = int(file.split("/")[-1].split(".")[0].split("_")[-1])
    if frequency not in table_dict:
        table_dict[frequency] = dict()
        if frequency != 0:
            amplitude[frequency] = None
    with open(file, 'r') as f:
        read_data = f.readlines()
    table_dict[frequency]['t'] = []
    table_dict[frequency]['p'] = []
    for i in range(1, len(read_data)):
        data = read_data[i].split(" ")
        if i == 1 or i == len(read_data)-1:
            table_dict[frequency]['t'].append(float(data[0]))
        x = float(data[1])
        y = float(data[2])
        z = float(data[3])
        table_dict[frequency]['p'].append(magnitude(x, y, z))
equalibrium = np.mean(table_dict[0]['p'])

for i in table_dict.keys():
    if i != 0:
        table_dict[i]['p'] -= equalibrium
        xMax = np.max(table_dict[i]['p'])
        xMin = np.min(table_dict[i]['p'])
        amplitude[i] = (xMax - xMin)/2

amplitude = pd.Series(amplitude).sort_index()
plt.scatter(amplitude.keys(), amplitude)
plt.plot(amplitude.keys(), amplitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Acceleration ($ms^{-2}$)")

plt.show()
