# This program prints out a random fruit
# Author: Gillian Kane-McLoughlin

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# Create an index - we want a random number refering to a fruits position in the index
# The position should be between 0 and the lenght -1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]

print("A Random Fruit:{}".format(fruit))
