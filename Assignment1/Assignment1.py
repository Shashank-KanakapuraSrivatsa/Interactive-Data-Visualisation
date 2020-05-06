import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

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

'''
for i in range(0,100):
    randomNumberList.append(random.randrange(0,max(len(x),len(y))))

for randomNumber in randomNumberList:
    del x[randomNumber]
    del y[randomNumber]
    del u[randomNumber]
    del v[randomNumber]    
'''
fig, ax = plt.subplots(figsize=(7,7))
ax.quiver(x,y,u,v,colorList)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

plt.show()