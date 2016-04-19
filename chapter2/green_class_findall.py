__author__ = 'JuHyeong Kim'
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")


# nameList = bsObj.findAll({"class":"green"})  ## wrong usage
nameList = bsObj.findAll("",{"class":"green"})
for name in nameList:
    print("name :",name)
    print(name.get_text())

