import sys
import os
import pandas as pd
import numpy as np
import math
import heapq
os.getcwd()
os.chdir('D:/D drive/CMPE 272/project')
df = pd.read_csv('housingData.csv',header = None,error_bad_lines=False)
df2 = pd.read_csv('public transport address process.csv',header = None,error_bad_lines=False)
df3 = pd.read_csv('whole foods address process.csv', header = None, error_bad_lines = False)
df4 = pd.read_csv('Park address process.csv', header = None, error_bad_lines = False)
df['shortest distance'] = 0
h = []
for i in range(1, df.shape[0]):
    for j in range(1, df2.shape[0]):
        lats = float(df.iloc[i, 4])
        late = float(df2.iloc[j, 1])
        lngs = float(df.iloc[i,5])
        lnge = float(df2.iloc[j,2])
        distance = math.acos(math.sin(math.pi*lats/180.0)*math.sin(math.pi*late/180.0)+math.cos(math.pi*lats/180.0)*math.cos(math.pi*late/180.0)*math.cos(math.pi*lngs/180.0-math.pi*lnge/180.0))*3963
        heapq.heappush(h, distance)
    df.iloc[i,9] = heapq.heappop(h)
df.iloc[0,9] = 'shortest distance to public trans'
df['shortest distance 2'] = 0
h = []
for i in range(1, df.shape[0]):
    for j in range(1, df3.shape[0]):
        lats = float(df.iloc[i, 4])
        late = float(df3.iloc[j, 1])
        lngs = float(df.iloc[i,5])
        lnge = float(df3.iloc[j,2])
        distance = math.acos(math.sin(math.pi*lats/180.0)*math.sin(math.pi*late/180.0)+math.cos(math.pi*lats/180.0)*math.cos(math.pi*late/180.0)*math.cos(math.pi*lngs/180.0-math.pi*lnge/180.0))*3963
        heapq.heappush(h, distance)
    df.iloc[i,10] = heapq.heappop(h)
df.iloc[0,10] = 'shortest distance to whole foods'
df['shortest distance 3'] = 0
h = []
for i in range(1, df.shape[0]):
    for j in range(1, df4.shape[0]):
        lats = float(df.iloc[i, 4])
        late = float(df4.iloc[j, 2])
        lngs = float(df.iloc[i,5])
        lnge = float(df4.iloc[j,3])
        distance = math.acos(math.sin(math.pi*lats/180.0)*math.sin(math.pi*late/180.0)+math.cos(math.pi*lats/180.0)*math.cos(math.pi*late/180.0)*math.cos(math.pi*lngs/180.0-math.pi*lnge/180.0))*3963
        heapq.heappush(h, distance)
    df.iloc[i,11] = heapq.heappop(h)
df.iloc[0,11] = 'shortest distance to parks'
df.to_csv('housing data with distance to transportation.csv', header = False, index = False)
