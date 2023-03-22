

import requests
from bs4 import BeautifulSoup
def donwloadsingle(newl):
    r=requests.get(newl).content
    s=BeautifulSoup(r,'lxml')
    f=s.find('li',class_='dowloads')
    newl=f.find('a')['href']
    return newl