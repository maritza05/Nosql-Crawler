# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen


htmlL = urlopen("http://stackoverflow.com/tags")
bsObjL = BeautifulSoup(htmlL, "html.parser")

nameLi = bsObjL.findAll("a", {"class": "post-tag"})


l = 0

while l < len(nameLi):
    html = urlopen("http://stackoverflow.com/tags/" +
                   nameLi[l].getText() + "/info")
    bsObj = BeautifulSoup(html, "html.parser")

    tagInfo = bsObj.findAll('div', {'class': 'post-text'})
    list = []
    m = 0
    while m < len(tagInfo):
        list.append(tagInfo[m].getText())
        m = m + 1
        str = list[0]
        str.strip(" ")
        print(str)


    # for tag in tagInfo:
        #info = tag.findAll('p')
        #print (info)

    print("*************************************************************")
    l = l + 1
