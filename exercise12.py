#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 12
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13)
'''
number = int(raw_input("Please enter a number\n"))

list = [1,1]
if number == 0:
    print(0)
elif number == 1:
    print(list[1])
else:
    for var in range(2,number):
        list.append(list[var-2] + list[var-1])
    print list
