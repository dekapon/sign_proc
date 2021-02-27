import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image, ImageDraw
from random import randint
from random import uniform

print(f'Hello world, exercise 2')
"""
print('Enter your name:')
x = 2
x = input()
x = int(x)
x = x + 2
print('Hello, ' + str(x))
"""
global m, n

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


def find_pixels(pixel_values):
    # load image, get image size
    result_x = []
    result_y = []
    for x in range(m):
        for y in range(m):
            if img.getpixel((x,y)) == pixel_values:
                # print("pixel pos = " + str(x) + " " + str(y))
                result_x.append(x)
                result_y.append(y)
    return result_x, result_y

def euclidean_distance():
    x = 0
    while x < len(result_x):
        # print("dist:" + str(math.sqrt((result_x[x]-greenPixelPosX[0]) ** 2 + (result_y[x]-greenPixelPosY[0]) ** 2)) )
        dist.append(math.sqrt((result_x[x]-greenPixelPosX[0]) ** 2 + (result_y[x]-greenPixelPosY[0]) ** 2))
        x += 1
    return dist


manual = 0
if manual:
    global m,n
    m, n = input("enter n and m:").split()

else:
    # print(ex_0(0, 10, 100))
    m = 100
    n = 100
    img = create_image(m, n)
    global result_x, result_y
    # result_x = []
    # result_y = []
    result_x, result_y = find_pixels((255, 0, 0))

    global greenPixelPosX, greenPixelPosY
    greenPixelPosX = []
    greenPixelPosY = []
    greenPixelPosX, greenPixelPosY = find_pixels((0, 255, 0))

    # print(type(greenPixelPosX[0]))
    # print(len(result_x))
    global dist
    dist = []
    dist = euclidean_distance()
    # print(dist)
    # print(len(result_y))
    # x = 2

    hist, bin_edges = np.histogram(dist)
    # plt.hist(dist)
    n, bins, patches =plt.hist(x=dist, bins=99, color='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    mean = sum(dist) / len(dist)
    dist = np.array(dist)
    print(dist.mean)
    print(type(dist.mean))
    plt.title('mean: ' + "{:.2f}".format(dist.mean()) + '   std: ' + "{:.2f}".format(dist.std()) + '   medi: ' + "{:.2f}".format(np.median(dist)))
    plt.show()
    # print(len(bins))
    # print(bin_edges)






