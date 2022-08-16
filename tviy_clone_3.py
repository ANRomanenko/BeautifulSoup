import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

PAGINATION = input('Введите число страниц для парсинга: ')
PAGINATION = int(PAGINATION.strip())

for count in range(1, PAGINATION + 1):
    print(f'Парсинг страницы № {count}')
    sleep(3)
    url = f'https://allo.ua/ru/processory/p-{count}/'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_='product-card')

    for i in data:

        title = i.find("a", class_='product-card__title').get_text(strip=True)
        product_link = i.find('div', class_='product-card__content').find('a').get('href')
        price = i.find('div', class_='v-price-box__cur').get_text(strip=True).replace(' ', '')[:-1]

        print(title + "\n" + product_link + "\n" + price + "\n\n")
