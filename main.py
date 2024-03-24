import requests as rq
from datetime import datetime

BASE_URL = 'http://winslinn.pythonanywhere.com/'

payload = {'input': 'Hello World!'}
response = rq.get(BASE_URL, params=payload)

json_values = response.json()

print(json_values['timestamp'])