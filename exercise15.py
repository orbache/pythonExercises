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

passLong = int(raw_input("Please enter the password long\n"))

a = int(random.uniform(1, passLong/4))
b = int(random.uniform(a, passLong/2 - a))
c = int(random.uniform(b, passLong/1.3 - a - b))
d = int(passLong - c - b - a)

lowerCaseList = random.sample(string.ascii_lowercase, a)
upperCaseList = random.sample(string.ascii_uppercase, b)
numbersList = random.sample(string.digits, c)
symbolsList = random.sample(string.punctuation, d)

newList = []
[newList.extend(digit) for digit in [lowerCaseList,upperCaseList,numbersList,symbolsList]]
random.shuffle(newList)
print ''.join(newList)

