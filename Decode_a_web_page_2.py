#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Evyatar Orbach"
__email__ = "evyataro@gmail.com"
'''Exercise 18
Using the requests and BeautifulSoup Python libraries, 
print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
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

for line in getContent('https://www.nbcnews.com/storyline/western-wildfires/california-s-biggest-wildfire-ever-still-growing-cancels-start-school-n898531'):
    print line