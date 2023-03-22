import requests
from bs4 import BeautifulSoup
import os


def watch(info, frame, dir,name):
    os.chdir(dir)
    url=frame['src']
    a = (f'''
<!DOCTYPE html>
<html >
    <body  bgcolor="black" style="color: floralwhite;">
            <h1>
            <a style="color: ghostwhite;" href="https://www.instagram.com/jidukrishnapj/">
                follow me on instagram
            </a>
            </h1>
            <p style="color:azure;">
            
            
            {str(info)}
            <h1>you are watching {str(name)}</h1>
            <iframe style="width: 686px; height: 386px;" allow="autoplay; encrypted-media" allowfullscreen="" class="metaframe rptss" frameborder="0" scrolling="no" src="{str(url)}"></iframe>
    
            </p>
        </body>
</html>

    ''')
    with open('movie.html', 'w', encoding="utf-8") as f:
        f.write(a)
    os.system('movie.html')
    return 'yes'

