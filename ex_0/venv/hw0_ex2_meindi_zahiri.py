import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image, ImageDraw
from random import randint
from random import uniform

print(f'Hello world, exercise 1')
"""
print('Enter your name:')
x = 2
x = input()
x = int(x)
x = x + 2
print('Hello, ' + str(x))
"""

def create_image(m, n):
    m = int(m)
    n = int(n)
    img = Image.new('RGB', (600, 600), color='white')
    #img.save('img.png')
    for x in range(m):
        for y in range(n):
            if uniform(0.0, 2.0) < 1.0:
                #img[m, n] = (0, 0, 0)
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 0, 0))

    green_x = randint(0,m*n-1)
    green_y = green_x
    green_x = green_x//m
    green_y = green_y % n

    img.putpixel((green_x, green_y), (0, 255, 0))
    img.show()


manual = 0
if manual:
    m, n = input("enter n and m:").split()

else:
    #print(ex_0(0, 10, 100))
    create_image(600, 600)







