from bs4 import BeautifulSoup
from urllib.request import urlopen

#html = urlopen("https://github.com/search?utf8=%E2%9C%93&q=mongodb")
html = urlopen("https://github.com/search?q=mongodb&type=Repositories&utf8=%E2%9C%93")
htmlC = urlopen("https://github.com/search?q=mongodb&type=Code&utf8=%E2%9C%93")
htmlI = urlopen("https://github.com/search?q=mongodb&type=Issues&utf8=%E2%9C%93")
htmlU = urlopen("https://github.com/search?q=mongodb&type=Users&utf8=%E2%9C%93")

infoObj = BeautifulSoup(html, "html.parser")
infoObjC = BeautifulSoup(htmlC, "html.parser")
infoObjI = BeautifulSoup(htmlI, "html.parser")
infoObjU = BeautifulSoup(htmlU, "html.parser")


info = infoObj.findAll('nav', {'class' : 'menu'})
infoC = infoObjC.findAll('nav',{'class' : 'menu'})
infoI = infoObjI.findAll('nav', {'class' : 'menu'})
infoU = infoObjU.findAll('nav', {'class' : 'menu'})

i = 0
listI = []
listG = []


while i < len(info):
    listI.append(info[i].getText())
    k = listI[0].split()
    #print ("a", k)
    i = i + 1

c = 0
listC = []

while c < len(infoC):
    listC.append(infoC[c].getText())
    co = listC[0].split()
    #print("b", co)
    c = c + 1

y = 0
listY = []

while y < len(infoI):
    listY.append(infoI[y].getText())
    yo = listY[0].split()
    #print("c", yo)
    y = y + 1


r = 0
listU = []

while r < len(infoU):
    listU.append(infoU[r].getText())
    us = listU[0].split()
    #print("d", us)
    r = r + 1


listG.append(k[0])
listG.append(co[1])
listG.append(yo[2])
listG.append(us[3])


for g in listG:
    print(g)


