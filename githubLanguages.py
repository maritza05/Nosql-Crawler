from bs4 import BeautifulSoup
from urllib.request import  urlopen

html = urlopen("https://github.com/search?utf8=%E2%9C%93&q=mongodb")
gitObj =  BeautifulSoup(html, "html.parser")

gitInfo =  gitObj.findAll('ul', {'class' : 'filter-list small'})
#print(gitInfo.getText())

g = 0
list = []

while g < len(gitInfo):
    list.append(gitInfo[g].getText())
    info = list[0].split()
    f = 0
    while f < len(info):
        print(info[f])
        f = f + 1
    #print(info[0])
    g = g + 1



#print(gitInfo)
