# Write a program that uses these two functions to count how many times the program has been run
# Author: Gillian Kane-McLoughlin

filename = "count.txt"

def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# main
num = readNumber()
num += 1
print ("we have run this program {} times".format(num))
writeNumber(num)