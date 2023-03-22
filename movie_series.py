import time
import mshtml
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
op=Options()
op.add_argument('--headless')
driver=webdriver.Chrome(options=op)
def mseries(url,dir):
    r=requests.get(url)
    b=BeautifulSoup(r.content,'lxml')
    info=b.find('div',{'id':'info'})
    f=b.find_all('div',class_='custom_fields')[-2:]

    for i in info:print(i.text)
    print('you have these many epi and seasons (plz note the data may not be 100% accurate):')
    s=int(input('season no:'))
    epi=int(input('epi no:'))
    link=list(url)[:-1]
    link=''.join(link)+f'-{s}x{epi}/'
    try:
        link=link.replace('tvseries','episodes')
    except:link=link.replace('tvshows','episodes')
    print('plz wait for 5 sec')
    print('''


    you may see some random text in the console but dont worry about it .


    ''')
    for i in range(3):
        try:
            driver.get(link)
            break
        except:
            print('im sleeping for 5 sec to avoid the traffic')
            driver.quit()
            time.sleep(5)
    time.sleep(3)
    b=BeautifulSoup(driver.page_source,'lxml')
    driver.quit()

    frame=b.find('iframe',class_='metaframe rptss')
    name=link.split('/')[-2]
    if len(f)==0:
        print('failed')
    else:
        return info,frame,dir,name
        #mshtml.watch(info,frame,dir,name)
    import os,sys

