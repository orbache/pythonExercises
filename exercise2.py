#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?
'''

number = raw_input("Please enter a number\n")
dividedNum = int(number) % 2
if not dividedNum:
    print("The number you picked is even\n")
else:
    print("The number you picked is odd\n")

