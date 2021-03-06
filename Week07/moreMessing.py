# Write a function that takes in a number and overwrites a file with that number (count.txt)
# Author: Gillian Kane-McLoughlin

fileName = "count.txt"

def writeFile(number):
    with open(fileName,"wt") as f:
        f.write(str(number))


writeFile(3)

