#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 15
Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
'''

import random
import string
random.seed = 1
lowerCaseList = random.sample(string.ascii_lowercase,3)
upperCaseList = random.sample(string.ascii_uppercase,3)
numbersList = random.sample(string.digits,3)
symbolsList = random.sample(string.punctuation,3)

newList = []
[newList.extend(digit) for digit in [lowerCaseList,upperCaseList,numbersList,symbolsList]]
random.shuffle(newList)
print ''.join(newList)

