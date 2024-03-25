from PIL import Image
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date
from io import BytesIO

import glob
import os
import requests
import easyocr

image_files = glob.glob(f'schedule/*', recursive=True)

schedule_URL = 'https://rfc.nubip.edu.ua/to-a-student/changes-to-the-schedule/'
user_headers = headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'}

#soup = BeautifulSoup(open('page.html', encoding='utf-8'), 'html.parser')

day = str(date.today()).split('-')[2]

for file in image_files:
    print(f'Delete {file} completed.')
    os.remove(file)
html = Request(schedule_URL, headers=user_headers)
soup = BeautifulSoup(urlopen(html), 'html.parser')
    
figure_list = soup.find_all('figure')
    
for element in figure_list:
    image_alt = element.find('img')['alt']
    
    if image_alt != 'logo_white':
        change_day = image_alt.split()[0]
        
        #image_src = element.find('img')['src']
        image_src = element.find('img')['data-src']
            
        if change_day >= day:
            image_content = requests.get(image_src, headers=user_headers).content
            image_path = f'schedule/{change_day}'
                
            with open(os.path.join('schedule/', f'{change_day}.webp'), 'wb') as f:
                f.write(image_content)
                
            image_content = Image.open(f'{image_path}.webp').convert('RGB')
            image_content.save(f'{image_path}.jpg', 'jpeg')
                
            width, height = image_content.size
            image_content = image_content.crop((135, 0, width/2, height))

            img_bytes = BytesIO()
            image_content.save(img_bytes, format='JPEG')
            img_bytes = img_bytes.getvalue()

            reader = easyocr.Reader(['uk'])
            text = reader.readtext(img_bytes, detail=0)

            print(text)