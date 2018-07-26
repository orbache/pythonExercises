#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 1
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

from datetime import datetime
year = datetime.now().strftime("%Y")
name = raw_input("Please enter your name\n")
age = raw_input("Please enter your age\n")
print("Hi %s,\nIn 100 year from now you will be %s and the year is going to be %s" %(name, str(int(age) + 100), str(int(year) + 100)))

