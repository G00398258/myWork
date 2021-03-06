# Week 07 lab - messing with files - create a text file with 0 in it
# Author: Gillian Kane-McLoughlin

with open ("count.txt", "wt") as testFile:
    testFile.write("0")