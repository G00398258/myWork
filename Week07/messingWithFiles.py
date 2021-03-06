# Week 07 lab - Write a function that reads in a number from a file that already exists(count.txt)
# test the program by calling the function and outputting the number
# Author: Gillian Kane-McLoughlin

fileName = "count.txt"

def readNumber():
    with open(fileName, "rt") as f:
        number = int(f.read())
        return number

num = readNumber()
print (num)