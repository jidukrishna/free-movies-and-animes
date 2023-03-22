import requests
from bs4 import  BeautifulSoup
def info(url):
    r=requests.get(url)
    s=BeautifulSoup(r.content,'lxml')
    f=s.find('div',class_='anime_info_body_bg')
    return f
