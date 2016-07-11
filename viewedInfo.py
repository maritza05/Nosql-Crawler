# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

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

    tagInfo = bsObj.findAll('table', {'id': 'qinfo'})
    list = []
    m = 0
    while m < len(tagInfo):
        list.append(tagInfo[m].getText())
        m = m + 1
        print(list[0])
    
    for child in bsObj.find("table",{"id":"giftList"}).children:    print(child)

    # for tag in tagInfo:
        #info = tag.findAll('p')
        #print (info)

    print("*************************************************************")
    l = l + 1
