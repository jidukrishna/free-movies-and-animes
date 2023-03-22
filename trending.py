import requests
from bs4 import BeautifulSoup
def top_anime(n):
    a={
        'd':('https://myanimelist.net/topanime.php','TOP ANIME'),
        'e':('https://myanimelist.net/topanime.php?type=airing','TOP AIRING'),
        'f':('https://myanimelist.net/topanime.php?type=tv','TOP TV SERIES'),
        'g':('https://myanimelist.net/topanime.php?type=movie','TOP MOVIES'),
        'h':('https://myanimelist.net/topanime.php?type=ova','TOP OVA'),
        'i':('https://myanimelist.net/topanime.php?type=special','TOP SPECIAL'),
        'j':('https://myanimelist.net/topanime.php?type=bypopularity','MOST POPUALR'),
        'k':('https://myanimelist.net/topanime.php?type=favorite','MOST FAVORITE')




}

    print(f'----------{a[n][1]}----------')
    link=a[n][0]
    r=requests.get(link).content
    s=BeautifulSoup(r,'lxml')
    f=s.find_all('div',class_='detail')
    t=s.find_all('div',class_='js-top-ranking-score-col di-ib al')
    c=1
    for i,j in zip(f,t):
        print(f'{c} : {i.text.strip()}  rating:{j.text.strip()}')
        c+=1