#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 10
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
'''

number = int(raw_input("Please enter a number\n"))
if len([var for var in range(1,number-1) if not number%var]) < 2:
    print "Primary"
else:
    print "Not primary"
