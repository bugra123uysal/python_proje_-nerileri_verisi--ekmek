import requests
from bs4 import BeautifulSoup

urlm='https://webrazzi.com/kategori/yazilim/'
 
al=requests.get(urlm)
içerikal=al.content
b=BeautifulSoup(içerikal,"html.parser")
türbelirle=b.find_all("h2")

for xx in türbelirle:
    print(xx.text)

