#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 9
Generate a random number between 1 and 9 (including 1 and 9). 
 the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
 (Hint: remember to use the user input lessons from the very first exercise)
'''

from random import randrange
number = randrange(1,9)
NumOfGuesses = 0
while(True):
    guess = int(raw_input("Please guess a number\n"))
    NumOfGuesses += 1
    if guess < number:
        print("your guess is too low\n")
    elif guess > number:
        print("your guess is too high\n")
    else:
        print("Bingo!!\n")
        print("You tried %d times\n" %NumOfGuesses)
        break

