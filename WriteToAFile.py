#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 20
Take the code from the How To Decode A Website exercise 
(if you didn’t do it or just want to play with some different code, use the code from the solution), 
and instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.
'''
import requests
from bs4 import  BeautifulSoup


def getContent(v_html):
    paragraphList = []
    r = requests.get(v_html)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content,'lxml')
        #title
        paragraphList.append(soup.title.get_text().strip())
        #second title
        paragraphList.append(soup.find_all(class_="dekSummary___GcgCT f4 f5-m f6-l f7-xl publico-hed lh-copy fw3 ls-normal mb3 mb6-m")[0].get_text().strip())
        #content
        for sentence in soup.find_all('p'):
            paragraphList.append(sentence.get_text().strip())
        return paragraphList

with open('/Users/eorbach/newFile.txt','w') as openFile:
    for line in getContent('https://www.nbcnews.com/storyline/western-wildfires/california-s-biggest-wildfire-ever-still-growing-cancels-start-school-n898531'):
        openFile.write(line.encode('utf-8'))
    openFile.close()
