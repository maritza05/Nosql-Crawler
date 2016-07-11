# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://stackoverflow.com/tags")
bsObj = BeautifulSoup(html, "html.parser")




nameLi = bsObj.findAll("a", {"class" : "post-tag"})
nameList = bsObj.findAll("span", {"class":"item-multiplier-count"})

dictionary = {}


li = 0

while li < len(nameList):
	dictionary [nameLi[li]. getText()] = [nameList[li].getText()]
	#print(nameLi[li].getText() + nameList[li].getText())
	li = li + 1

for d in dictionary:
	print(d, "-", dictionary[d])