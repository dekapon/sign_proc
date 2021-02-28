print(f'Hello world, exercise 4')
from numpy import random
import numpy as np
import math
import matplotlib.pyplot as plt

from hw0_ex1_meindi_zahiri import ex_0
# import hw0_ex1_meindi_zahiri

global x, y

"""
Just need to change degenerate to 1 or offset to 1. Don't put both of them at 1
"""
vectorSize = 10
degenerate = 0
offset = 0


x=random.randint(100, size=(vectorSize))
if offset:  # gives 2
    y = x + 2
elif degenerate:  # gives 0
    y = x
else:
    y=random.randint(100, size=(vectorSize))

# res = x - y
# res = res ** 2
# res = np.mean(res, axis=0)
# res = np.sqrt(res)

if degenerate:
    res = np.sqrt(((x - y) ** 2).mean())
print(ex_0(0, 100, 100))

t = np.linspace(0, 2*math.pi, 400)
a = np.sin(t)
plt.plot(t, a, 'r') # plotting t, a separately
plt.show()



