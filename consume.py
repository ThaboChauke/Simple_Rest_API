import os
import random
import requests


random_number = random.randint(1,10)
link = f'http://127.0.0.1:8000/quotes/{random_number}'
response = requests.get(link)
print(response.json())