# -*- coding: utf-8 -*-
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen


htmlL = urlopen("http://stackoverflow.com/tags")
bsObjL = BeautifulSoup(htmlL, "html.parser")

nameLi = bsObjL.findAll("a", {"class": "post-tag"})


l = 0

while l < len(nameLi):
    http = httplib2.Http()
    status, response = http.request('http://www.stackoverflow.com/tags/'+nameLi[l].getText()+'/info')

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_attr('href'):
            print(link['href'])
            #print(nameLi[l].getText())
    print("************************************************************************************")
    l = l + 1



