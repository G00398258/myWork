# Same code as scatterPlot except we need to add label to the plot and set the titles and labels on the axis
# Author: Gillian Kane-McLoughlin

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)

plt.scatter(ages, salaries, label="salaries")
#plt.show() # if you do this the proram will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself
plt.plot(xpoints, ypoints, color='r', label = "x squared")

#Other labels
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()

# plt.show()

# Save this to a file called “prettier-plot.py”
plt.savefig('prettier-plot.png')
