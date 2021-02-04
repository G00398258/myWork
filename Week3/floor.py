# This program will floor a number (round a number down - need to import math module)
# Author: Gillian Kane-McLoughlin

import math

numberToFloor = float(input("Please enter a number with a decimal point: "))
flooredNumber = math.floor(numberToFloor)

print ("{} floored is {}".format(numberToFloor,flooredNumber))