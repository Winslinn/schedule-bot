from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date

import glob
import os
import urllib.request

jpg_files = glob.glob(f'schedule/**/*.jpg', recursive=True)

schedule_URL = 'https://rfc.nubip.edu.ua/to-a-student/changes-to-the-schedule/'
user_headers = headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'}

html = Request(schedule_URL, headers=user_headers)
soup = BeautifulSoup(urlopen(html), 'html.parser')

#soup = BeautifulSoup(open('page.html', encoding='utf-8'), 'html.parser')

day = str(date.today()).split('-')[2]

if len(jpg_files) > 0:
    for file in jpg_files:
        print(f'Delete {file} completed.')
        os.remove(file)
else:
    figure_list = soup.find_all('figure')
    
    for element in figure_list:
        image_alt = element.find('img')['alt']
        
        if image_alt != 'logo_white':
            change_day = image_alt.split()[0]
        
            #image_src = element.find('img')['src']
            image_src = element.find('img')['data-src']
            
            if change_day > day:
                print(image_src)
                image_content = urllib.request.urlretrieve(image_src, f'schedule/{change_day}.webp')