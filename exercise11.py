#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 11
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
'''

a = [5, 10, 15, 20, 25, 67]


def newFunc(list):
    newList = [list[0],list[len(list)-1]]
    return newList

print(newFunc(a))