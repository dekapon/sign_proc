# imports
from skimage import io, filters
from skimage import color
import matplotlib.pyplot as plt
import numpy as np

def mask(filename):
    # load image
    image = io.imread('Train-Data/SRF/input' + filename + '.png')
    #plt.rcParams['image.cmap'] = 'gray'
    #image = color.rgb2gray(image)

    

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

    return sel