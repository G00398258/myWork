# This program will calculate a person's Body Mass Index (BMI)
# Author: Gillian Kane-McLoughlin

height = int(input('Please enter your height in cm: '))
weight = int(input('Please enter your weight in kg: '))

# First convert height to meters
heightm = height / 100

# Now convert to meters squared
heightm2 = heightm * heightm

# Calculate BMI
BMI = weight / heightm2

# Print the result
print ('Your BMI is: ' + str(BMI))