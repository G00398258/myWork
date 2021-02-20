# This program reads in a string and strips any leading or trailing spaces
# It also converts all the letters to lower case and outputs the lenght of the original string
# and the normalised one
# Author: Gillian Kane-McLoughlin

rawString = input("Please enter a string with spaces and both upper and lower characters: ")

# Normalise the inputted string using strip and lower functions
normalisedString = rawString.strip().lower()

# Calculate the lenght of the two variables
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print("That String normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalised))