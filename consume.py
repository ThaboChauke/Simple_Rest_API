import requests
from dotenv import loadenv


response = requests.get('host')
print(response.json())