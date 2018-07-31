#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 14
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

import string

str = raw_input("Please enter your string\n")

def delimiterHandler(v_str,v_delimiter):
    return string.split(str,v_delimiter, )

def reverseString(v_list):
    newList = []
    i = len(v_list)-1
    while i >= 0:
        newList.append(v_list[i])
        i -= 1
    return ' '.join(newList)

print reverseString(delimiterHandler(str,' '))
