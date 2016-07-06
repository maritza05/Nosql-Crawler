from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://stackoverflow.com/tags")
bsObj = BeautifulSoup(html, "html.parser")

diccionario = {}


nameLi = bsObj.findAll("a", {"class" : "post-tag"})
nameList = bsObj.findAll("span", {"class":"item-multiplier-count"})

diccionario = {}


li = 0

while li < len(nameList):
	diccionario [nameLi[li]. getText()] = [nameList[li].getText()]
	#print(nameLi[li].getText() + nameList[li].getText())
	li = li + 1

for d in diccionario:
	print(d, "-", diccionario[d])

