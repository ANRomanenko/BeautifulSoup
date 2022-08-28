import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://tviy.club/'
URL = 'https://tviy.club/sumki-genskiekoganye-genskie-sumki/2686-sumki-genskiekoganye-genskie-sumki'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_content(html):
    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all('div', class_='product-thumb')
    cards = []
    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='product-name').get_text(strip=True)
            }
        )
    return cards


def save_doc(items, path):
    with open(path, "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название карточки товара'])
        for item in items:
            writer.writerow([item['title']])


def parser():
    PAGINATION = input('Введите число страниц для парсинга: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGINATION + 1):
            print(f'Парсинг страницы №: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        print('Парсирнг завершён! Скачено', len(cards), 'карточек товара!')


parser()