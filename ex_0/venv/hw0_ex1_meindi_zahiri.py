print(f'Hello world, exercise 1')

import matplotlib.pyplot as plt
import numpy as np
import math

"""
print('Enter your name:')
x = 2
x = input()
x = int(x)
x = x + 2
print('Hello, ' + str(x))
"""
def ex_0(a,b,c):
    manual = 1
    if manual:
        a, b, c = input("the 3 numbers:").split()
        a = int(a)
        b = int(b)
        c = int(c)
        error = 0
        if a >= 0 and b >= 0:
            x = np.linspace(a, b, c)
        else:
            error = 1
    else:
        x = np.linspace(-10,10,100)
    if not(error):
        y = np.arctan(np.tan(2*math.pi*x))
        plt.plot(x,y)
        plt.show()
        return 0
    else:
        return -1



