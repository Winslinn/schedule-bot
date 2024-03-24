from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import glob
import os

scd_path = '/home/Winslinn/mysite/schedule'
jpg_files = glob.glob(f'{scd_path}/**/*.jpg', recursive=True)

schedule_URL = 'https://rfc.nubip.edu.ua/to-a-student/changes-to-the-schedule/'
html = Request(schedule_URL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'})

soup = BeautifulSoup(urlopen(html), 'html.parser')

if len(jpg_files) > 0:
    for file in jpg_files:
        print(f'Delete {file}')
        os.remove(file)
else:
    print(soup.find('img', class_='stk-img wp-image-7649', attrs={"name": "data-src"}))
    print('hello')