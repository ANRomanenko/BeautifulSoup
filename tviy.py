import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
HOST = 'https://tviy.club/'
URL = 'https://tviy.club/sumki-genskiekoganye-genskie-sumki/2686-sumki-genskiekoganye-genskie-sumki'


# Получаем html (запрашиваем через requests)
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


# html = get_html(URL) # проверка нашего кода
# print(html)

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-thumb')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='product-name').get_text(strip=True),
                'link_product': item.find('div', class_='product-name').find('a').get('href'),
                'product-model': item.find('div', class_='product-model').get_text(strip=True),
                'price': item.find('div', class_='price').get_text(strip=True)[:-7]
            }
        )
    print(cards[0])

html = get_html(URL)
get_content(html.text)