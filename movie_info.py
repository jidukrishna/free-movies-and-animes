import os
import time
import mshtml
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

op = Options()
op.add_argument('--headless')
driver = webdriver.Chrome(options=op)
os.system('cls')


def mseries(url, dir):
    r = requests.get(url)
    name = url.split('/')[-2]
    b = BeautifulSoup(r.content, 'lxml')
    info = b.find('div', {'id': 'info'})
    print('plz wait for 5 sec')
    print('''
    
    
    you may see some random text in the console but dont worry about it .
    
    
    ''')
    for i in range(3):
        try:
            driver.get(url)
            break
        except:
            print('im sleeping for 5 sec to avoid the traffic')
            driver.quit()
            time.sleep(5)
    time.sleep(3)
    b = BeautifulSoup(driver.page_source, 'lxml')
    driver.quit()

    frame = b.find('iframe', class_='metaframe rptss')
    return info, frame, dir, name
