# Write a program that plots the function y = x*2
# Author: Gillian Kane-McLoughlin

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # x squared - multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()
