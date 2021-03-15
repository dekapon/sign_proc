import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from random import uniform
from random import randint
import numpy as np
import time

print(f'Hello world homework 1 ex 3')
t = time.time()

def lin_int(y_vals, x):
    pass

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

    green_x = randint(0,m*n-1)
    green_y = green_x
    green_x = green_x//m
    green_y = green_y % n

    img.putpixel((green_x, green_y), (0, 255, 0))
    # img.show()
    plt.imshow(img)
    plt.show()
    img.save('img.png')
    return img

def createGrayscale(m,n):
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
    #create new image
    result = Image.new('RGB', (scaling_factor * m, 1), color='white') # 1 is n
    for x in range(m):
        for y in range(scaling_factor):
            # put here an if for multichannel to apply to the 3 channels
            if multichannel:
                pass # change this
            else:
                result.putpixel((x*scaling_factor+y, 0), signal.getpixel((x, 0)))

    return result

def rescaling_1D(signal, scaling_factor):
    width, height = signal.size
    # print("width: " + str(width) + " height: " + str(height))
    #create new image
    result = Image.new('RGB', (scaling_factor * m, 1), color='white') # 1 is n
    for x in range(m):
        for y in range(scaling_factor):
            # print("x: " + str(x) + " y: " + str(y) + "new x: " + str(x*scaling_factor+y))
            result.putpixel((x*scaling_factor+y, 0), signal.getpixel((x, 0)))

    return result


m = 10  # width
n = 1  # height
img = create_image(m, n)

newimage = rescaling_1D(img, 4)
plt.imshow(newimage)
plt.show()

# 3.2.1
grayscaleImage = createGrayscale(4,4)
grayscaleImageRescaled = rescaling_2D(grayscaleImage,2,False)
plt.imshow(grayscaleImage)
plt.imshow(grayscaleImageRescaled)
plt.show()


elapsed = time.time() - t
print("done, elapsed time: " + str(elapsed) + " s")



