import numpy as np 
from matplotlib import pyplot as plt
import seaborn as sns 
import math
import datetime


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
unique,count = np.unique(inputData,return_counts=True)
plt.title('Histogram')
plt.xlabel('Data Values')
plt.ylabel('Absolute Occurences')
plt.plot(unique,count)
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
#plt.show()


##----------------------------------------------------------------------------##
## e) Histogram Equalisation
##----------------------------------------------------------------------------##
def readInput(filename):
    rawInputDataAllBands = np.loadtxt(filename, delimiter=",", dtype=str)
    cleanedInputDataAllBands = np.core.defchararray.replace(rawInputDataAllBands,'\"','')
    inputDataAllBands = cleanedInputDataAllBands.astype(np.float64)
    return inputDataAllBands[::-1]

inputDataBand1 = readInput("i170b1h0_t0.txt")
inputDataBand2 = readInput("i170b2h0_t0.txt")
inputDataBand3 = readInput("i170b3h0_t0.txt")
inputDataBand4 = readInput("i170b4h0_t0.txt")

def histogramEqualisation(inputDataBand):
    r,p = np.unique(inputDataBand,return_counts=True)
    sumOfP = np.sum(p)
    pr = p/sumOfP
    CDF = np.zeros(len(pr))
    for index, value in enumerate(pr):
        CDF[0] = pr[0]
        if index > 0:
            CDF[index] = pr[index] + CDF[index-1]
    s = np.multiply(CDF,255)
    s = s.astype('int')
    sRedistributed = np.zeros((len(inputDataBand),len(inputDataBand)))
    for i in range(len(inputDataBand)):
        for j in range(len(inputDataBand[i])):
            element = inputDataBand[i][j]
            indexOfElementInR = np.where(r == element)
            sRedistributed[i][j] = s[indexOfElementInR]
    return sRedistributed

histogramEqualisation1 = histogramEqualisation(inputDataBand1)
histogramEqualisation2 = histogramEqualisation(inputDataBand2)
histogramEqualisation3 = histogramEqualisation(inputDataBand3)
histogramEqualisation4 = histogramEqualisation(inputDataBand4)

fig,axes = plt.subplots(2,2)
axes[0,0].set_title('i170b1h0.fit_0')
axes[0,0].imshow(histogramEqualisation1, cmap='gray')
axes[0,0].xaxis.grid(True)
axes[0,0].yaxis.grid(True)
axes[0,1].set_title('i170b2h0.fit_0')
axes[0,1].imshow(histogramEqualisation2, cmap='gray')
axes[0,1].xaxis.grid(True)
axes[0,1].yaxis.grid(True)
axes[1,0].set_title('i170b3h0.fit_0')
axes[1,0].imshow(histogramEqualisation3, cmap='gray')
axes[1,0].xaxis.grid(True)
axes[1,0].yaxis.grid(True)
axes[1,1].set_title('i170b4h0.fit_0')
axes[1,1].imshow(histogramEqualisation4, cmap='gray')
axes[1,1].xaxis.grid(True)
axes[1,1].yaxis.grid(True)
plt.show()

##----------------------------------------------------------------------------##
## f) RGB Image for Histogram Equalised
##----------------------------------------------------------------------------##
#Reference : https://stackoverflow.com/questions/10443295/combine-3-separate-numpy-arrays-to-an-rgb-image-in-python
stackedArray = np.dstack([histogramEqualisation4, histogramEqualisation3, histogramEqualisation1]).reshape((500, 500, 3))
plt.imshow(np.uint8(stackedArray*-255))
plt.title("RGB Image with datasets b4=r, b3=g, b1=b")
plt.grid()
plt.show()