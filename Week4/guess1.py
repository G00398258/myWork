# program that prompts the user to guess a number and keeps prompting the user to guess the number 
# until the user gets the right one
# Author: Gillian Kane-McLoughlin

numtoguess = 6

guess = int(input("Guess a number between 1 and 10: "))
while (guess != numtoguess):
    print ("Wrong!")
    guess = int(input("Please guess again: ")) # need to remember to keep this indented

print ("Correct! The number was", numtoguess)
