#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 5
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''

listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,13]
listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newList = []
listA.sort()
listB.sort()
for itemA in listA:
    if itemA in listB and itemA not in newList:
        newList.append(itemA)


print newList

