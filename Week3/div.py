# This program will read in two numbers and divide the first by the second 
# giving the integer result and remainder
# Author: Gillian Kane-McLoughlin

# Ask user to input values for numbers and convert to int
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Calculations
result = x // y
remainder = x % y

# Print the result
print ("{} divided by {} is {} with remainder {}".format(x, y, result, remainder)) 