from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://github.com/search?q=mongodb&type=Users&utf8=%E2%9C%93")
infoObj = BeautifulSoup(html, "html.parser")

info = infoObj.findAll('nav', {'class' : 'menu'})

i = 0
listI = []

while i < len(info):
    listI.append(info[i].getText())
    print (listI[0])
    i = i + 1



