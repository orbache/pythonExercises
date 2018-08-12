#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 19
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
'''

def IsTheNumberInside(v_list,v_number):
    for item in v_list:
        if v_number == item:
            return True
    return False

print IsTheNumberInside([1,3,5,7,8], 4)