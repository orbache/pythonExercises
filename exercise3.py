#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 3
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''

newList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 0, 1, 55, 89, 3, 5]

for var in newList:
    if var < 5:
        print(var)