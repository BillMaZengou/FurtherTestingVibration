import glob
from os import path
import numpy as np
import pandas as pd

table_dict = dict()
i = 0
for file in glob.glob("../result/Ex2/*/*"):  # The path should change
    i += 1
    frequency = file[-3:] if file[-3] != '/' else file[-2:]
    frequency = int(frequency)
    if frequency not in table_dict:
        table_dict[frequency] = dict()
    file = file + "/filesEx2Result.txt"
    if path.exists(file):
        with open(file, 'r') as f:
            read_data = f.readlines()

        for x in range(1, len(read_data)): # probably remove the first answer as many report that they have no time to respond
        # for x in range(len(read_data)):
            data_item = read_data[x]
            item = data_item.split(",")[0].split(" ")
            waveform = item[0]
            direction = item[1]
            if waveform not in table_dict[frequency]:
                table_dict[frequency][waveform] = dict()
            if direction not in table_dict[frequency][waveform]:
                table_dict[frequency][waveform][direction] = []
            table_dict[frequency][waveform][direction].append(1)
print("There are {} people's results".format(i//5))
for i in table_dict.keys():
    for j in table_dict[i].keys():
        for k in table_dict[i][j].keys():
            table_dict[i][j][k] = sum(table_dict[i][j][k])
df1 = pd.DataFrame(table_dict)
df1 = df1.sort_index(0)
df1 = df1.sort_index(1)
# print(df1)
# print()

table_dict1 = table_dict.copy()
for i in table_dict1.keys():
    for j in table_dict1[i].keys():
        if "Up" not in table_dict1[i][j]:
            a = 0
        else:
            a = table_dict1[i][j]["Up"]
        if "Down" not in table_dict1[i][j]:
            b = 0
        else:
            b = table_dict1[i][j]["Down"]

        table_dict1[i][j] = "{}/{}".format(a, (a+b))

table_dict2 = table_dict.copy()
for i in table_dict2.keys():
    for j in table_dict2[i].keys():
        [a, b] = table_dict2[i][j].split("/")
        [a, b] = [int(a), int(b)]
        table_dict2[i][j] = int(a/b * 100)
df2 = pd.DataFrame(table_dict2)
df2 = df2.sort_index(0)
df2 = df2.sort_index(1)
# print(df2)
# print()

table_dict3 = table_dict.copy()
for i in table_dict3.keys():
    for j in table_dict3[i].keys():
        if abs(table_dict2[i][j]-50) <= 20:
            table_dict2[i][j] = 'X'
df3 = pd.DataFrame(table_dict3)
df3 = df3.sort_index(0)
df3 = df3.sort_index(1)
# print(df3)
# print()
