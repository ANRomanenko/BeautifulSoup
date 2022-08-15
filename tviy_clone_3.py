import requests
from bs4 import BeautifulSoup

url = 'https://allo.ua/ru/processory/'

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, 'lxml')
cards = []
for item in soup.find_all():
    print(item)