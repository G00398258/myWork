# program that prompts the user to guess a number and keeps prompting the user to guess the number 
# until the user gets the right one - it will also tell them if the number is too high or low
# Author: Gillian Kane-McLoughlin

numtoguess = 12
guess = int(input("Guess a number between 0 and 20: "))
while guess != numtoguess:
    if guess < numtoguess:
            print ("Too low")
    else:
            print ("Too high")
    guess = int(input("Please guess again: "))

print ("Yes! The number was", numtoguess)