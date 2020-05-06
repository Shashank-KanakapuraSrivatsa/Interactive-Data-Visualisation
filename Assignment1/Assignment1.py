import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x,y,z,u,v,w = [],[],[],[],[],[]
with open('field2.irreg.txt','r') as fileHandle:
    for i in range(0,6):
        fileHandle.readline()
    inputLine = [line.rstrip() for line in fileHandle]

for singleLine in inputLine:
    values = singleLine.split(' ')
    x.append(float(values[0]))
    y.append(float(values[1]))
    z.append(float(values[2]))
    u.append(float(values[3]))
    v.append(float(values[4]))
    w.append(float(values[5]))

fig, ax = plt.subplots()

ax.quiver(x,y,u,v)
plt.show()