#!/usr/bin/python
__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 16
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''

import requests
from bs4 import BeautifulSoup
titleList = []

page = requests.get("https://www.nytimes.com/")
soap = BeautifulSoup(page.content,'html.parser')


for title in soap.find_all(["title","h1","h2","h3"]):
    if title.string is not None:
        titleList.append(title.string)

for title in titleList:
    print title
