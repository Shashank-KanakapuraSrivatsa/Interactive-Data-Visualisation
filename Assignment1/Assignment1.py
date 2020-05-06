import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
import matplotlib.cm as cm
from matplotlib.colors import Normalize

x,y,u,v = [],[],[],[]
randomNumberList = []
colorList = []
with open('field2.irreg.txt','r') as fileHandle:
    for i in range(0,6):
        fileHandle.readline()
    inputLine = [line.rstrip() for line in fileHandle]

for singleLine in inputLine:
    values = singleLine.split(' ')
    x.append(float(values[0]))
    y.append(float(values[1]))
    u.append(float(values[3]))
    v.append(float(values[4]))
    colorList.append(np.sqrt(((float(values[3])))**2 +((float(values[4])))**2))

for i in range(0,3000):
    randomNumberList.append(random.randrange(0,max(len(x),len(y))))


for randomNumber in randomNumberList:
    if(randomNumber < len(x) and randomNumber < len(y)):
        x[randomNumber] = 0.0
        y[randomNumber] = 0.0
        u[randomNumber] = 0.0
        v[randomNumber] = 0.0

fig, ax = plt.subplots(figsize=(12,12))
q = ax.quiver(x,y,u,v,colorList,scale=2)
ax.xaxis.set_ticks([min(x),max(x),0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
ax.yaxis.set_ticks([min(y),max(y),0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
ax.set_title('Water flow velocity visualisation')
ax.set_xlabel('X equivalent of vectors')
ax.set_ylabel('Y equivalent of vectors')
ax.set_aspect('equal')
fig.colorbar(q,label='Velocity')
plt.show()