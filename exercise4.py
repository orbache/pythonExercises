#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 4
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don\'t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

divisorList = []
number = int(raw_input("Please enter a number\n"))
divide = number-1
while divide > 1:
    if not (number % divide):
        divisorList.append(divide)
    divide -=1

print divisorList




