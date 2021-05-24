# imports
from skimage import io, filters
from skimage import color
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from skimage.morphology import disk
from skimage import restoration
from skimage.filters import sobel
from skimage import measure
from skimage.util import crop


def mask(filename):
    # load image
    image = io.imread('Train-Data\input' + filename + '.png')

    # cropping
    top = 15
    right = 12
    bottom = 35
    bottom = 250 # test
    left = 50
    image = crop(image, ((top, bottom), (left, right), (0, 0)), copy=False)

    plt.rcParams['image.cmap'] = 'gray'
    image = color.rgb2gray(image)

    # pre
    size = (3, 3)
    im_open = ndimage.grey_opening(image, size=size)
    im_median = ndimage.median_filter(im_open, size=5)

    # edge detect
    edge_median = ndimage.sobel(im_median, axis=0)  # x
    #sx = ndimage.sobel(im_median, axis=0) # x
    #sy = ndimage.sobel(im_median, axis=1) # y
    #edge_median = np.hypot(sx, sy)

    # perform inverse binary thresholding
    sigma = 10
    blur = filters.gaussian(image, sigma=sigma)
    t = 0.3
    mask = blur > t

    # use the mask to select the "interesting" part of the image
    #sel = np.zeros_like(image)
    #sel[mask] = edge_median[mask]

    im_masked = np.zeros_like(image)
    im_masked[mask] = im_median[mask]

    # mask for edges
    #mask2 = sel > 0.6


    # segmentation
    level1 = 0.5
    level2 = 0.4
    level3 = 0.09
    gray_r = im_masked.reshape(im_masked.shape[0] * im_masked.shape[1])
    for i in range(gray_r.shape[0]):
        if gray_r[i] > level1:
            gray_r[i] = 3
        elif gray_r[i] > level2:
            gray_r[i] = 2
        elif gray_r[i] > level3:
            gray_r[i] = 1
        else:
            gray_r[i] = 0
    im_segmented = gray_r.reshape(im_masked.shape[0], im_masked.shape[1])
    plt.imshow(im_segmented, cmap='gray')
    plt.show()

    # find contours
    contours = np.asarray(measure.find_contours(im_segmented, level=2)) # between 2 and 3
    test0 = contours[0]
    test1 = contours[1]
    test2 = contours[2]
    test3 = contours[3]
    nbreContours = contours.shape[0]
    test = test0[0,1]
    testt = contours[0][0,1]
    for i in range(nbreContours):
        if contours[i][0,1] == 0.0:
            print(i)
    # plot contours
    fig, ax = plt.subplots()
    ax.imshow(im_segmented, cmap=plt.cm.gray)

    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

    plt.show()