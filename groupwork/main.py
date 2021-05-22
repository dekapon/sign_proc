# imports
from skimage import io, filters
from scipy import ndimage
from skimage import color
import matplotlib.pyplot as plt
import numpy as np
from imageio import imread
import cv2
import mask

# Call of the mask
#filename = '_1647_1'
filename = '_1494_1'
ROI = mask.mask(filename)
print("ROI shape")
print(ROI.shape)

# Edges
'''
edge = ndimage.sobel(ROI, axis=0)
plt.title('Edges')
plt.imshow(edge)

plt.show()
'''
## Clustering
#img = cv2.imread('Train-Data/SRF/input' + filename + '.png')
img = ROI[:, :, :3]
img = ndimage.filters.gaussian_filter(img, sigma = 1.5)
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)
print(Z.shape)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)
K = 4
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()


edge = ndimage.sobel(res2, axis=1)
plt.title('Edges')
plt.imshow(edge)


plt.show()