import numpy as np 
from matplotlib import pyplot as plt
import seaborn as sns 
import math
import statistics
rawData = np.fromfile("slice150.raw", dtype='int16', count=-1, sep='')
structuredData = rawData.reshape([512,512])

##----------------------------------------------------------------------------##
## a) Profile Line
##----------------------------------------------------------------------------##
profileLine = structuredData[255]
plt.title('Profile Line (Line 256)')
plt.plot(profileLine)
plt.show()
plt.clf()

##----------------------------------------------------------------------------##
## b) Mean value and Variance value
##----------------------------------------------------------------------------##
print('Mean value : ', np.mean(structuredData))
print('Variance value : ', np.var(structuredData))

##----------------------------------------------------------------------------##
## c) Histogram
##----------------------------------------------------------------------------##
sns.set_style('whitegrid')
sns.distplot(structuredData, hist_kws={"histtype": "bar", "alpha": 0.4, "color": "g"}, color='black')
plt.title('Histogram')
plt.show()
plt.rcParams['axes.grid'] = False


##----------------------------------------------------------------------------##
## d) Linear transformation
##----------------------------------------------------------------------------##
#S=T(r)=((r-rmin)/(rmax-rmin))*Smax
sMax = 255
rMin = structuredData.min()
rMax = structuredData.max()
n = len(structuredData)
linearTransformedMatrix = np.zeros(shape=(n,n))
def linearTransformation(r):
    s=((r-rMin)/(rMax-rMin))*sMax
    return int(s)
for i in range(len(structuredData)):
    for j in range(len(structuredData[i])):
        r = structuredData[i][j]
        if r < rMin:
            s = rMin
        elif r > rMax:
            s = sMax
        else :
            s = linearTransformation(r)
            
        linearTransformedMatrix[i][j] = s

plt.title('Linear Transformation')
plt.imshow(linearTransformedMatrix, 'gray')
plt.show()


##----------------------------------------------------------------------------##
## e) Non-Linear transformation
##----------------------------------------------------------------------------##
#T(r) = c*log2((1+r)), where c = sMax / log2(1+rMax)
nonLinearTransformedMatrix = np.zeros((n,n))
c = sMax / (math.log((1+rMax),2))
for i in range(len(structuredData)):
    for j in range(len(structuredData[i])):
        r = structuredData[i][j]
        s = int(c * (math.log((1+r),2)))
        nonLinearTransformedMatrix[i][j] = s
plt.title('Non-Linear Transformation')
plt.imshow(nonLinearTransformedMatrix, cmap='gray')
plt.show()


##----------------------------------------------------------------------------##
## f) Boxcar smoothing filter
##----------------------------------------------------------------------------##
boxCarFilter = np.zeros((11,11))
smoothingOutput = np.zeros((512,512))
denominator = 11 * 11
def boxCarFilterCalculator(structuredData,i,j,boxCarFilter):
    sum = 0
    for row in range(i-math.floor((len(boxCarFilter))/2),i+math.floor((len(boxCarFilter))/2)-1):
        for col in range(j-math.floor((len(boxCarFilter))/2),j+math.floor((len(boxCarFilter))/2)-1):
            sum = sum + structuredData[row][col]
    return (sum/denominator)

for i in range(len(structuredData)):
    if i >= (0+math.floor((len(boxCarFilter))/2)) and i <= (len(structuredData)-math.floor((len(boxCarFilter))/2)) :
        for j in range(len(structuredData[i])):
            if j >= (0+math.floor((len(boxCarFilter))/2)) and j <= (len(structuredData)-math.floor((len(boxCarFilter))/2)) :
                value = boxCarFilterCalculator(structuredData,i,j,boxCarFilter)
                smoothingOutput[i][j] = value
            
plt.title('Box Car Smoothing Filter')
plt.imshow(smoothingOutput,'gray')
plt.show()





##----------------------------------------------------------------------------##
## g) Median filter
##----------------------------------------------------------------------------##
medianFilter = np.zeros((11,11))
medianOutput = np.zeros((512,512))
denominator = 11 * 11
def medianFilterCalculator(structuredData,i,j,medianFilter):
    medianList = []
    for row in range(i-math.floor((len(boxCarFilter))/2),i+math.floor((len(boxCarFilter))/2)-1):
        for col in range(j-math.floor((len(boxCarFilter))/2),j+math.floor((len(boxCarFilter))/2)-1):
            medianList.append(structuredData[row][col])
    return statistics.median(medianList)

for i in range(len(structuredData)):
    if i >= (0+math.floor((len(boxCarFilter))/2)) and i <= (len(structuredData)-math.floor((len(boxCarFilter))/2)) :
        for j in range(len(structuredData[i])):
            if j >= (0+math.floor((len(boxCarFilter))/2)) and j <= (len(structuredData)-math.floor((len(boxCarFilter))/2)) :
                value = medianFilterCalculator(structuredData,i,j,medianFilter)
                medianOutput[i][j] = value
            
plt.title('Median Filter')
plt.imshow(medianOutput,'gray')
plt.show()