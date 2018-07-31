#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 6
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

str = raw_input("Please enter a string\n")
str1 = str[::-1]

if str1 == str:
    print("The string you entered is palindrome")
else:
    print("The string you entered is NOT palindrome")
