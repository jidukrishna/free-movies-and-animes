import time

import requests
from bs4 import BeautifulSoup
import movie_series


def ms(dir):
    while True:
        link = 'https://netmovies.to/?s='
        name = input('movie/series search:').strip().lower()
        name = name.split(' ')
        name = '+'.join(name)
        link = link + name

        r = requests.get(link)
        b = BeautifulSoup(r.content, 'lxml')
        f = b.find_all('div', class_='no-result animation-2')
        if len(f) == 0:
            f = b.find_all('div', class_='result-item')
            c = 1
            ml = {}
            for i in f:
                print(f'''{c} : {i.find('div', class_='title').text}''')
                try:
                    print(i.find('span', class_='rating').text, '  year :', i.find('span', class_='year').text)
                    print(' ')
                except:
                    pass

                ml[c] = i.find('a')['href']
                c += 1
            choice = int(input('your choice (eg : 1):'))
            link = ml[choice]
            a = link.split('/')
            if 'tvshows' in a or 'tvseries' in a:
                type = 'series'

                # movie_series.mseries(link,dir)

            elif 'movies' in a:
                type = 'movies'

            else:
                type = ('invalid')
            return type, link, dir

        else:
            print('not found')
            break
