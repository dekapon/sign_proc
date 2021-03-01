print(f'Hello world, exercise 4')
from numpy import random
import numpy as np
import math
import matplotlib.pyplot as plt
import time

def ex_0(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    x = np.linspace(a, b, c)
    if a >= 0 and b >= 0:
        y = np.arctan(np.tan(2 * math.pi * x))
        plt.plot(x, y)
    return y

"""
Just need to change degenerate to 1 or offset to 1. Don't put both of them at 1
"""
def rmse(a, b):
    vectorSize = 10
    degenerate = 0
    offset = 0


    a=random.randint(100, size=(vectorSize))
    if offset:  # gives 2
        b = a + 2
    elif degenerate:  # gives 0
        b = a
    else:
        b=random.randint(100, size=(vectorSize))

    # res = x - y
    # res = res ** 2
    # res = np.mean(res, axis=0)
    # res = np.sqrt(res)

    res = np.sqrt(((a - b) ** 2).mean())
    print(res)
    return res

t = np.linspace(0, 100, 100)

# add if phase fixed
# phase = math.pi / 2

phase = math.pi
steps = 10
rmseData = []
for counter in range(steps):
    x = np.cos(4 * math.pi * t + phase * counter / steps)
    y = ex_0(0, 100, 100)
    plt.plot(t, x, 'r')
    plt.show()
    time.sleep(0.1)
    rmseData.append(rmse(x,y))
print(rmseData)



