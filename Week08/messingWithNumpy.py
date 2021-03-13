# Part 1 of Week 08 lab
# Author: Gillian Kane-McLoughlin

import numpy as np

# Write a program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000)
minSalaray = 20000
maxSalary = 80000
numberofEntries = 10

# Modify the program so that the “random” salaries are the same each time the program is run
np.random.seed(1)
salaries = np.random.randint(minSalaray, maxSalary, numberofEntries)
print (salaries)

# Modify the program, to make another array of numbers that has the salaries plus 5000 
salariesPlus = salaries + 5000
print (salariesPlus)

# Modify the program so that it increases all the salaries by 5% (store in another array)
# My code
fivepc = (salaries / 100) * 5
modSalaries = salaries + fivepc
# Convert to int array and print
incSalaries = modSalaries.astype(int)
print (incSalaries)

# Andrew's code
salariesMult = salaries * 1.05 # add 5% by multiplying by 1.05
print(salariesMult)
# This is a float array, here I convert it to an int array (it does a floor)
newSalaries = salariesMult.astype(int)
print(newSalaries)
