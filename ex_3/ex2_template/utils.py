from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import random
import os.path
from imageio import imread


##############################################################################
#                        Functions for you to complete                       #
##############################################################################

################
# EXERCISE 2.1 #
################


def compute_ssd(patch, mask, texture, patch_half_size):
    # For all possible locations of patch in texture_img, computes sum square
    # difference for all pixels where mask = 0
    #
    # Inputs:
    #   patch: numpy array of size (2 * patch_half_size + 1, 2 * patch_half_size + 1, 3)
    #   mask: numpy array of size (2 * patch_half_size + 1, 2 * patch_half_size + 1)
    #   texture: numpy array of size (tex_rows, tex_cols, 3)
    #
    # Outputs:
    #   ssd: numpy array of size (tex_rows - 2 * patch_half_size, tex_cols - 2 * patch_half_size)

    # patch_rows, patch_cols = np.shape(patch)[0,1]
    patch_rows, patch_cols = np.shape(patch)[:2]
    assert patch_rows == 2 * patch_half_size + 1 and patch_cols == 2 * patch_half_size + 1, "patch size and patch_half_size do not match"
    # tex_rows, tex_cols = np.shape(texture)[0:1]
    tex_rows, tex_cols = np.shape(texture)[:2]
    ssd_rows = tex_rows - 2 * patch_half_size
    ssd_cols = tex_cols - 2 * patch_half_size
    ssd = np.zeros((ssd_rows, ssd_cols))

    mask_idx = (mask == 255)
    patch[mask_idx] = 0

    for ind, value in np.ndenumerate(ssd):
        #
        # ADD YOUR CODE HERE
        #
        x, y = ind
        offset_x = x + patch_half_size
        offset_y = y + patch_half_size
        local_tex = texture[
                    offset_x - patch_half_size: offset_x + patch_half_size + 1,
                    offset_y - patch_half_size: offset_y + patch_half_size + 1,
                    :]
        ssd[x, y] = np.power(np.sum(patch - local_tex), 2)




    return ssd


################
# EXERCISE 2.2 #
################


def copy_patch(img, mask, texture, iPatchCenter, jPatchCenter, iMatchCenter, jMatchCenter, patch_half_size):
    # Copies the patch of size (2 * patch_half_size + 1, 2 * patch_half_size + 1)
    # centered on (iMatchCenter, jMatchCenter) in texture into the image
    # img with center coordinates (iPatchCenter, jPatchCenter) for each
    # pixel where mask = 1.
    #
    # Inputs:
    #   img: ndarray of size (im_rows, im_cols, 3)
    #   mask: numpy array of size (2 * patch_half_size + 1, 2 * patch_half_size + 1)
    #   texture: numpy array of size (tex_rows, tex_cols, 3)
    #   iPatchCenter, jPatchCenter, iMatchCenter, jMatchCenter, patch_half_size: integers
    #
    # Outputs:
    #   res: ndarray of size (im_rows, im_cols, 3)

    patchSize = 2 * patch_half_size + 1
    iPatchTopLeft = iPatchCenter - patch_half_size
    jPatchTopLeft = jPatchCenter - patch_half_size
    iMatchTopLeft = iMatchCenter - patch_half_size
    jMatchTopLeft = jMatchCenter - patch_half_size
    temp = texture[iMatchTopLeft : iMatchTopLeft + patchSize, jMatchTopLeft : jMatchTopLeft + patchSize, :]
    mask_idx = (mask == 255)
    # if mask == 255:
    #     mask_idx = True
    # res = img
    for i in range(patchSize):
        for j in range(patchSize):
            if mask_idx[i, j]:
                img[iPatchTopLeft + i, jPatchTopLeft + j, :] = temp[i, j, :]

    return img


def find_edge(mask):
    # Returns the edges of a binary mask image.
    # The result edge_mask is a binary image highlighting the edges
    [cols, rows] = np.shape(mask)
    edge_mask = np.zeros(np.shape(mask))
    for y in range(rows):
        for x in range(cols):
            if (mask[x, y]):
                if (mask[x - 1, y] == 0 or mask[x + 1, y] == 0 or mask[x, y - 1] == 0 or mask[x, y + 1] == 0):
                    edge_mask[x, y] = 1
    return edge_mask
