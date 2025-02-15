""" 1 Linear filtering """

# Imports
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
import time
import pdb

img = plt.imread('cat.jpg').astype(np.float32)

plt.imshow(img)
plt.axis('off')
plt.title('original image')
plt.show()

# 1.1
def boxfilter(n):
    # this function returns a box filter of size nxn
    result = np.array([[1/(n*n)] * n for i in range(n)])
    return result

# 1.2
# Implement full convolution
def myconv2(image, filt):
    # This function performs a 2D convolution between image and filt, image being a 2D image. This
    # function should return the result of a 2D convolution of these two images. DO
    # NOT USE THE BUILT IN SCIPY CONVOLVE within this function. You should code your own version of the
    # convolution, valid for both 2D and 1D filters.
    # INPUTS
    # @ image         : 2D image, as numpy array, size mxn
    # @ filt          : 1D or 2D filter of size kxl
    # OUTPUTS
    # img_filtered    : 2D filtered image, of size (m+k-1)x(n+l-1)

    ### your code should go here ###
    # prenier nombre = nbre colonnes
    #print(image.width)
    filt = np.flip(filt, 0)
    filt = np.flip(filt, 1)
    m = len(image)
    n = len(image[0])
    k = filt.shape[0]
    l = filt.shape[1]
    expandedMatrix = np.array([[0] * (m+k-1) for i in range(n+l-1)])
    for i in range(m):
        for j in range(n):
            #print("i:" + str(i) + "   j: " + str(j))
            #print("iter i:" + str(i+(k-1)/2) + "   j: " + str(j+(l-1)/2))
            expandedMatrix[i+int((k-1)/2)][j+int((l-1)/2)] = image[i][j]
    result = expandedMatrix
    #print(result)
    # looping through the result matrice
    for i in range (int((k-1)/2),m):
        for j in range (int((l-1)/2),n):
            # looping through the small matrice
            tempValue = 0 # value used for the sum
            for o in range(k):
                for p in range(l):
                    #if (i<0 or j<0 or i>=m or j>=n): # we add 0
                       # pass
                    #else:
                        #tempValue = tempValue + filt[k][l] * image[i][j]
                    tempValue = tempValue + expandedMatrix[i+o-1][j+p-1] * filt[o][p]
            print(tempValue)
            result[i][j] = tempValue
                    #print(expandedMatrix[i+o-1][j+p-1])
            #flip
    print(result)
    return result


# 1.3
# create a boxfilter of size 11 and convolve this filter with your image - show the result
bsize = 11

### your code should go here ###


# 1.4
# create a function returning a 1D gaussian kernel
def gauss1d(sigma, filter_length=11):
    # INPUTS
    # @ sigma         : sigma of gaussian distribution
    # @ filter_length : integer denoting the filter length
    # OUTPUTS
    # @ gauss_filter  : 1D gaussian filter

    ### your code should go here ###

    return gauss_filter


# 1.5
# create a function returning a 2D gaussian kernel
def gauss2d(sigma, filter_size=11):
    # INPUTS
    # @ sigma         : sigma of gaussian distribution
    # @ filter_size   : integer denoting the filter size
    # OUTPUTS
    # @ gauss2d_filter  : 2D gaussian filter

    ### your code should go here ###

    return gauss2d_filter

# Display a plot using sigma = 3
sigma = 3

### your code should go here ###


# 1.6
# Convoltion with gaussian filter
def gconv(image, sigma):
    # INPUTS
    # image           : 2d image
    # @ sigma         : sigma of gaussian distribution
    # OUTPUTS
    # @ img_filtered  : filtered image with gaussian filter

    ### your code should go here ###

    return img_filtered


# run your gconv on the image for sigma=3 and display the result
sigma = 3

### your code should go here ###


# 1.7
# Convolution with a 2D Gaussian filter is not the most efficient way
# to perform Gaussian convolution with an image. In a few sentences, explain how
# this could be implemented more efficiently and why this would be faster.
#
# HINT: How can we use 1D Gaussians?

### your explanation should go here ###

# 1.8
# Computation time vs filter size experiment
size_range = np.arange(3, 103, 5)
t1d = []
t2d = []
for size in size_range:
    pass
    ### your code should go here ###



image = plt.imread("cat.jpg")
filt = boxfilter(3)

image = np.array([[10, 11, 10, 0, 0, 1],
[9, 11, 10, 1, 0, 1],
[10, 9, 10, 0, 2, 1],
[11, 10, 9, 10, 9, 11],
[9, 10, 11, 9, 9, 11],
[10, 9, 9, 11, 10, 10]])

filt = np.array([[1, 1, 1],
[1, 1, 1],
[1, 1, 1]])
filt = filt / 9
myconv2(image,filt)

# plot the comparison of the time needed for each of the two convolution cases
plt.plot(size_range, t1d, label='1D filtering')
plt.plot(size_range, t2d, label='2D filtering')
plt.xlabel('Filter size')
plt.ylabel('Computation time')
plt.legend(loc=0)
plt.show()
