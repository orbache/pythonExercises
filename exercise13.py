#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 13
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''

listA = [1, 3, 4, 5, 5, 6, 6, 7, 1, 3]

def throwDuplicates(listA):
    sett = set()

    for item in range(len(listA)):
        sett.add(listA[item])

    return list(sett)

print throwDuplicates(listA)