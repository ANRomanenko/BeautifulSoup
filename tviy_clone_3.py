import requests
from bs4 import BeautifulSoup

url = 'https://allo.ua/ru/processory/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)