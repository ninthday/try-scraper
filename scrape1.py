from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.nccu.edu.tw")
objbs = BeautifulSoup(html.read(), "html.parser")
print(objbs.title)

for link in objbs.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs["href"])