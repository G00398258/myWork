# this program reads in a student's percentage mark and
# prints out the corresponding grade 
# (the program should also check that the percentage is valid)
# Author: Gillian Kane-McLoughlin

mark = float(input("Please enter the percentage mark received (without % symbol): "))
if mark <0 or mark >100:
    print ("Percentage mark entered invalid - input should be between 0 & 100")
elif mark < 40:
    print ("Fail")
elif mark >= 40 and mark <= 49:
    print ("Pass")
elif mark >= 50 and mark <= 59:
     print ("Merit 2")
elif mark >= 60 and mark <= 69:
     print ("Merit 1")
else: # only one option left
    print ("Distinction")
