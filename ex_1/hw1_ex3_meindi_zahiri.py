import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from random import uniform
from random import randint
import numpy as np
import time
import os

from decimal import *

print(f'Hello world homework 1 ex 3')
t = time.time()


# def interp(y_vals, x_vals, x_new):
#     y_new = []
#     for i in range(x_new.size):
#         if x_new[i] >= np.min(x_vals) and x_new[i] <= np.max(x_vals):
#             ytemp = y_vals[i](1 - (x_new[i] - x_vals[i]) / (x_vals[i + 1] - x_vals[i])) + y_vals[i + 1](x_new[i] - x_vals[i]) / (x_vals[i + 1] - x_vals[i])
#             y_new.append(ytemp)
#         else:
#             y_new.append(y_vals[i])
#     return y_new

def interp(y_vals, x_vals, x_new):
    size_new = len(x_new)
    size_values = len(x_vals)
    y_new = np.empty(size_new)

    for i in range(size_new):
        if x_new[i] <= x_vals[0]:
            y_new[i] = y_vals[0]
        elif x_new[i] >= x_vals[size_values - 1]:
            y_new[i] = y_vals[size_values - 1]
        else:
            j = np.searchsorted(x_vals, x_new[i])
            dx = x_vals[j] - x_vals[j - 1]
            dy = y_vals[j] - y_vals[j - 1]
            y_new[i] = y_vals[j - 1] + ((x_new[i] - x_vals[j - 1]) * dy / dx)

    return y_new


def test_interp():
    # Tests the interp() function with a known input and output
    # Leads to error if test fails

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([0.2, 0.4, 0.6, 0.4, 0.6, 0.8, 1.0, 1.1])
    x_new = np.array((0.5, 2.3, 3, 5.45))
    y_new_solution = np.array([0.2, 0.46, 0.6, 0.69])
    y_new_result = interp(y, x, x_new)
    np.testing.assert_almost_equal(y_new_solution, y_new_result)


def interp_1D(signal, scale_factor):
    # Linearly interpolates one dimensional signal by a given saling fcator
    #
    # Inputs:
    #   signal: A one dimensional signal to be samples from, numpy array
    #   scale_factor: scaling factor, float
    #
    # Outputs:
    #   signal_interp: Interpolated 1D signal, numpy array

    signal_interp = interp(signal, np.linspace(1, len(signal), len(signal)),
                           np.linspace(1, len(signal), int(scale_factor * len(signal))))

    return signal_interp


def test_interp_1D():
    # Test the interp_1D() function with a known input and output
    # Leads to error if test fails

    y = np.array([0.2, 0.4, 0.6, 0.4, 0.6, 0.8, 1.0, 1.1])
    y_rescaled_solution = np.array([
        0.20000000000000001, 0.29333333333333333, 0.38666666666666671,
        0.47999999999999998, 0.57333333333333336, 0.53333333333333333,
        0.44000000000000006, 0.45333333333333331, 0.54666666666666663,
        0.64000000000000001, 0.73333333333333339, 0.82666666666666677,
        0.91999999999999993, 1.0066666666666666, 1.0533333333333335,
        1.1000000000000001
    ])
    y_rescaled_result = interp_1D(y, 2)
    np.testing.assert_almost_equal(y_rescaled_solution, y_rescaled_result)


def interp_2D(img, scale_factor):
    # Applies bilinear interpolation using 1D linear interpolation
    # It first interpolates in one dimension and passes to the next dimension
    #
    # Inputs:
    #   img: 2D signal/image (grayscale or RGB), numpy array
    #   scale_factor: Scaling factor, float
    #
    # Outputs:
    #   img_interp: interpolated image with the expected output shape, numpy array
    rows = len(img)
    # print(rows)
    columns = len(img[0])
    tempVector = np.array([[0] * int(columns * scale_factor) for i in range(rows)]).astype(float)
    for i in range(rows):
        tempVector[i, :] = np.array(interp_1D(img[i, :], scale_factor))
    img_interp = np.array([[0] * int(columns * scale_factor) for i in range(int(rows * scale_factor))]).astype(float)
    for i in range(int(columns * scale_factor)):
        img_interp[:, i] = np.array(interp_1D(tempVector[:, i], scale_factor))
    # print(len(img_interp))
    return img_interp


def test_interp_2D():
    # Tests interp_2D() function with a known and unknown output
    # Leads to error if test fails

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_scaled = np.array([[1., 1.4, 1.8, 2.2, 2.6, 3.],
                              [2., 2.4, 2.8, 3.2, 3.6, 4.],
                              [3., 3.4, 3.8, 4.2, 4.6, 5.],
                              [4., 4.4, 4.8, 5.2, 5.6, 6.]])

    result = interp_2D(matrix, 2)
    np.testing.assert_almost_equal(matrix_scaled, result)


# ex 3.1.2
def create_image(m, n):
    m = int(m)
    n = int(n)
    global img
    img = Image.new('RGB', (m, n), color='white')
    # img.save('img.png')
    for x in range(m):
        for y in range(n):
            if uniform(0.0, 2.0) < 1.0:
                # img[m, n] = (0, 0, 0)
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 0, 0))

    green_x = randint(0, m * n - 1)
    green_y = green_x
    green_x = green_x // m
    green_y = green_y % n

    img.putpixel((green_x, green_y), (0, 255, 0))
    # img.show()
    plt.imshow(img)
    plt.show()
    img.save('img.png')
    return img


def createGrayscale(m, n):
    m = int(m)
    n = int(n)
    global img
    img = Image.new('1', (m, n), color='white')
    for x in range(m):
        for y in range(n):
            if uniform(0.0, 2.0) < 1.0:
                # img[m, n] = (0, 0, 0)
                img.putpixel((x, y), (0))
            else:
                img.putpixel((x, y), (1))

    plt.imshow(img)
    plt.show()
    img.save('img.png')
    return img


def rescaling_2D(signal, scaling_factor, multichannel):
    width, height = signal.size
    # create new image
    result = Image.new('RGB', (scaling_factor * m, 1), color='white')  # 1 is n
    for x in range(m):
        for y in range(scaling_factor):
            # put here an if for multichannel to apply to the 3 channels
            if multichannel:
                pass  # change this
            else:
                result.putpixel((x * scaling_factor + y, 0), signal.getpixel((x, 0)))
    return result


def interp_3D(img, scale_factor):
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]
    # for i in range(3):
    r_rescaled = interp_2D(r, scale_factor)
    print("r channel done")
    g_rescaled = interp_2D(g, scale_factor)
    print("g channel done")
    b_rescaled = interp_2D(b, scale_factor)
    print("b channel done")
    return np.dstack((r_rescaled,g_rescaled,b_rescaled))
    # return Image.merge("RGB", (r, g, b))


def rescaling_1D(signal, scaling_factor):
    width, height = signal.size
    # print("width: " + str(width) + " height: " + str(height))
    # create new image
    result = Image.new('RGB', (scaling_factor * m, 1), color='white')  # 1 is n
    for x in range(m):
        for y in range(scaling_factor):
            # print("x: " + str(x) + " y: " + str(y) + "new x: " + str(x*scaling_factor+y))
            result.putpixel((x * scaling_factor + y, 0), signal.getpixel((x, 0)))

    return result


test = True
if test:
    filename = 'bird.jpg'
    filename = 'lenna.jpg'
    # filename = 'butterfly.jpg'
    scale_factor = 1.5  # Scaling factor
    # scale_factor = 5  # Scaling factor
    print('...................................................')
    # print('Testing test_interp()...')
    # test_interp()
    # print('done.')
    #
    # print('Testing interp_1D()....')
    # test_interp_1D()
    # print('done.')
    #
    # print('Testing interp_2D()....')
    # test_interp_2D()
    # print('done.')

    print('Testing bilinear interpolation of an image...')
    # Read image as a matrix, get image shapes before and after interpolation
    img = (plt.imread(filename)).astype('float')  # need to convert to float
    in_shape = img.shape  # Input image shape

    # Apply bilinear interpolation
    # print(len(img.shape))
    if (len(img.shape) == 1):
        img_int = interp_2D(img, scale_factor)
    else:
        img_int = interp_3D(img, scale_factor)
    print('done.')

    # Now, we save the interpolated image and show the results
    print('Plotting and saving results...')
    plt.figure()
    plt.imshow(img_int.astype('uint8'))  # Get back to uint8 data type
    filename, _ = os.path.splitext(filename)
    plt.savefig('{}_rescaled.jpg'.format(filename))
    plt.close()

    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(img.astype('uint8'))
    plt.title('Original')
    plt.subplot(1, 2, 2)
    plt.imshow(img_int.astype('uint8'))
    plt.title('Rescaled by {:2f}'.format(scale_factor))
    print('Do not forget to close the plot window --- it happens:) ')
    plt.show()

    print('done.')


else:
    m = 10  # width
    n = 1  # height
    img = create_image(m, n)

    newimage = rescaling_1D(img, 4)
    plt.imshow(newimage)
    plt.show()

    # 3.2.1
    grayscaleImage = createGrayscale(4, 4)
    grayscaleImageRescaled = rescaling_2D(grayscaleImage, 2, False)
    plt.imshow(grayscaleImage)
    plt.imshow(grayscaleImageRescaled)
    plt.show()

elapsed = time.time() - t
print("done, elapsed time: " + str(elapsed) + " s")
