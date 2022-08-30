import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

PAGINATION = input('Введите число страниц для парсинга: ')
PAGINATION = int(PAGINATION.strip())


def download(url):
    resp = requests.get(url, stream=True)
    r = open("C:\\Романенко Андрей\\image\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1, PAGINATION + 1):
        print(f'Парсинг страницы №: {count}')
        url = f'https://allo.ua/ru/processory/p-{count}/'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_='product-card')

        for i in data:

            product_link = i.find('div', class_='product-card__content').find('a').get('href')
            yield product_link


def array():
    for product_link in get_url():

        response = requests.get(product_link, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_='p-view__main p-main--without-connect')
        try:
            name = data.find('picture', class_='main-gallery__link').find('img').get('title')
        except AttributeError:
            continue
        salesman = data.find('div', class_='shipping-seller__brand shipping-brand').find('span').get_text(strip=True)
        price = data.find('span', class_='sum').get_text(strip=True).replace(' ', '')[:-2]
        characteristic = data.find('td', class_='product-details__value').get_text(strip=True)
        availability = data.find('p', class_='p-trade__stock-label').get_text(strip=True).replace('✓', '')
        link_image = data.find('picture', class_='main-gallery__link').find('img').get('src')
        download(link_image)
        yield name, str(salesman), price, characteristic, availability, link_image












    # for i in data:
    #
    #     title = i.find("a", class_='product-card__title').get_text(strip=True)
    #     product_link = i.find('div', class_='product-card__content').find('a').get('href')
    #     price = i.find('div', class_='v-price-box__cur').get_text(strip=True).replace(' ', '')[:-1]
    #
    #     print(title + "\n" + product_link + "\n" + price + "\n\n")
