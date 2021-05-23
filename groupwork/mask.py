# imports
from skimage import io, filters
from skimage import color
import matplotlib.pyplot as plt
import numpy as np

from skimage.util import crop

def mask(filename):



    # load image
    image = io.imread('Train-Data/SRF/input' + filename + '.png')
    #plt.rcParams['image.cmap'] = 'gray'
    #image = color.rgb2gray(image)


    # cropping
    top = 15
    right = 12
    bottom = 35
    bottom = 250 # test
    left = 50
    image = crop(image, ((top, bottom), (left, right), (0, 0)), copy=False)

    #blur the image
    sigma = 5
    blur = color.rgb2gray(image)
    blur = filters.gaussian(blur, sigma = sigma)

    # perform inverse binary thresholding
    t = 0.3
    mask = blur > t

    # use the mask to select the "interesting" part of the image
    sel = np.zeros_like(image)
    sel[mask] = image[mask]

    # result of mask fct
    plt.subplot(1, 3, 1)
    plt.title('Original image')
    plt.imshow(image)

    plt.subplot(1,3,2)
    plt.title('Mask')
    plt.imshow(mask)

    plt.subplot(1,3,3)
    plt.title('ROI')
    plt.imshow(sel)

    plt.show()

    # envelope detection probleme si concave
    test = np.argwhere(mask)
    minMax = np.zeros((test.shape[0],2))

    # for i in range (test.shape[0]):
        # np.min(test[i,:])
        # if test[:,1] == i:
    minMax = np.zeros((mask.shape[1], 2))
    testy = mask.shape[0] # y
    testx = mask.shape[1] # x
    for x in range(mask.shape[1]):
        detected = 0
        for y in range(mask.shape[0]):
            if (mask[y,x] == True and detected == 0):
                minMax[x,0] = y
                detected = 1

    for x in range(mask.shape[1]):
        detected = 0
        for y in range(mask.shape[0]-1,-1,-1):
            if (mask[y,x] == True and detected == 0):
                minMax[x,1] = y
                detected = 1

    x = np.linspace(0,507, 507)
    minMax[:, 0] = minMax[:,0]
    minMax[:, 1] = minMax[:,1]
    plt.show()

    # put envelope on image
    superposition = image
    for x in range(mask.shape[1]):
        superposition[int(minMax[x,0]),x] = [255, 0, 0, 255]
        superposition[int(minMax[x,1]),x] = [255, 0, 0, 255]
    # print(int(minMax[0,0]))

    # for x in range(30):
    #     for y in range(30):
    #         superposition[x, y] = [255, 0, 0, 255]

    plt.imshow(superposition)
    plt.show()
    return sel