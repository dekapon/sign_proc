import matplotlib.pyplot as plt
import numpy as np
import math

print(f'Hello world, exercise 1')
"""
print('Enter your name:')
x = 2
x = input()
x = int(x)
x = x + 2
print('Hello, ' + str(x))
"""

def ex_0(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    x = np.linspace(a, b, c)
    if a >= 0 and b >= 0:
        y = np.arctan(np.tan(2 * math.pi * x))
        plt.plot(x, y)
        plt.show()
        return 0
    else:
        return -1


manual = 0
if manual:
    a, b, c = input("the 3 numbers:").split()
    print(ex_0(a, b, c))
else:
    print(ex_0(0, 10, 100))






