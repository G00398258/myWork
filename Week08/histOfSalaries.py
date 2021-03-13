# Write a program that plots a histogram of the salaries (from messingWithNumpy)
# Author: Gillian Kane-McLoughlin

import numpy as np
import matplotlib.pyplot as plt

# Write a program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000)
minSalaray = 20000
maxSalary = 80000
numberofEntries = 10

# Modify the program so that the “random” salaries are the same each time the program is run
np.random.seed(1)
salaries = np.random.randint(minSalaray, maxSalary, numberofEntries)

plt.hist(salaries)
plt.show()
