import requests
from bs4 import BeautifulSoup
import os
def watch(url,dow,info,epi,dir):
    r=requests.get(url)
    s=BeautifulSoup(r.content,'lxml')
    f=s.find('li',class_='streamsb')
    stream=f.find('a')['data-video']



    f=s.find('li',class_='doodstream')
    ddos=f.find('a')['data-video']
    a=(f'''
<!DOCTYPE html>
<html >
    <body  bgcolor="black" style="color: floralwhite;">
            <h1>
          <a style="color: ghostwhite;" href="https://www.instagram.com/jidukrishnapj/">
                follow me on instagram
            </a>
            </h1>
            {str(info)}
            <p style="color:azure;">
                <h1>you are watching {str(epi)} </h1>
                <iframe id="embedvideo" src="{str(stream)}" allowfullscreen="true" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" style="width: 686px; height: 386px;"></iframe>
                <iframe id="embedvideo" src="{str(ddos)}" allowfullscreen="true" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" style="width: 686px; height: 386px;"></iframe>
            
            <a href="{str(dow)}">
            <br style="background-color: white;"> CLICK HERE FOR DOWNLOAD LINK
                </a>
        
            
            </p>
        </body>
</html>
    
    ''')
    with open('anime.html', 'w', encoding="utf-8") as f:
        f.write(a)
    return 'yes'