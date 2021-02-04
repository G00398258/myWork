# This program will read in two numbers and subracts the second number from the first
# Author: Gillian Kane-McLoughlin

# Ask user to input values for numbers and convert to int
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Calculate result
answer = x - y

# Print the result
print ("{} minus {} is {}".format(x, y, answer))