import numpy as np 
from matplotlib import pyplot as plt
import seaborn as sns 
import math

##----------------------------------------------------------------------------##
## Read input data from the file
##----------------------------------------------------------------------------##
rawInputData = np.loadtxt("i170b2h0_t0.txt", delimiter=",", dtype=str)
cleanedInputData = np.core.defchararray.replace(rawInputData,'\"','')
inputData = cleanedInputData.astype(np.float64)
inputData = inputData[::-1]

##----------------------------------------------------------------------------##
## a) Min value, Max value, Mean value and Variance value
##----------------------------------------------------------------------------##
print('Min value : ', np.min(inputData))
print('Max value : ', np.max(inputData))
print('Mean value : ', np.mean(inputData))
print('Variance value : ', np.var(inputData))

##----------------------------------------------------------------------------##
## b) Profile Line
##----------------------------------------------------------------------------##
coordinateArray = np.where(inputData == np.amax(inputData))
maxValueCoOrdinates = list(zip(coordinateArray[0], coordinateArray[1]))
for coordinate in maxValueCoOrdinates:
    profileLineCoordinate = coordinate
rowIndex = profileLineCoordinate[0]
plt.title('Profile Line (Max value)')
plt.xlabel('Position on x-axis')
plt.ylabel('Data values')
plt.plot(inputData[rowIndex])
plt.show()

##----------------------------------------------------------------------------##
## c) Histogram
##----------------------------------------------------------------------------##
unique,indices = np.unique(inputData,return_counts=True)
plt.title('Histogram (unique occurences)')
plt.xlabel('Data Values')
plt.ylabel('Occurences')
plt.plot(unique,indices)
plt.show()

##----------------------------------------------------------------------------##
## d) Rescaling values using non-linear transformation
#Below formula is used for transformation
#T(r) = c*log2((1+r)), where c = sMax / log2(1+rMax)
##----------------------------------------------------------------------------##
sMax = 255
rMin = inputData.min()
rMax = inputData.max()
n = len(inputData)
nonLinearTransformedMatrix = np.zeros((n,n))
c = sMax / (math.log((1+rMax),2))
for i in range(len(inputData)):
    for j in range(len(inputData[i])):
        r = inputData[i][j]
        s = int(c * (math.log((1+r),2)))
        nonLinearTransformedMatrix[i][j] = s
plt.title('Rescaling using Non-Linear Transformation')
plt.imshow(nonLinearTransformedMatrix, cmap='gray')
plt.colorbar(label='Rescaled Values')
plt.show()

