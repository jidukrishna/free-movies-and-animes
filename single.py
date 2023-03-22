
import requests
from bs4 import BeautifulSoup
def single_epi():
    while True:
        s=input('anime name:')

        se=s.strip().replace(' ','%20')
        a=f'https://gogoanime.gr/search.html?keyword={se}'
        r=requests.get(a).content
        soup=BeautifulSoup(r,'lxml')
        a=soup.find_all('p',class_='name')
        c=1
        d={}
        if len(a)!=0:
            for i in a:
                print(f'{c} : {i.text.strip()}')
                d[c]='https://gogoanime.gr'+i.find('a')['href']
                c+=1
            choice=int(input('ch:'))
            r=requests.get(d[choice])
            s=BeautifulSoup(r.content,'lxml')
            g=s.find('a',class_='active')
            print(f'This many epi are available:{g["ep_end"]}')
            epi=int(input('which epi:'))
            if epi>int(g['ep_end']):
                print('no epi found')
            else:
                b=d[choice].split('/')[-1]
                newl=f'https://gogoanime.gr/{b}-episode-{epi}'
                infourl=f'https://gogoanime.gr/category/{b}'
                return newl,str(b)+' epi no- '+str(epi),infourl
        else:print('anime not found')

