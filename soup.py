import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/com" class="sister" id="link3">Tillie</a>;
<a href="http://example.com/com1" class="sister" id="link3">Tillie</a>;
<a href="http://example.com/com3" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


url = 'https://allo.ua/ru/products/mobile/klass-kommunikator_smartfon/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='product-card')

cards = []

for item in items:
    cards.append(
        {
            'link':item.find('div', class_='product-card__content').find('a').get('href'),
            'title': item.find('div', class_='product-card__content').find('a').get('title')
        }
    )
print(cards)

# soup = BeautifulSoup(html_doc, 'lxml')
# print(len(soup.contents))
# print(soup.contents[0].name)

# url = 'https://allo.ua/ru/products/mobile/klass-kommunikator_smartfon/'
#
# response = requests.get(url)

# soup = BeautifulSoup(html_doc, 'lxml')


# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'lxml')
# comment = soup.b.string
# print(type(comment))
# print(soup.b.prettify())


# doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "lxml")
# footer = BeautifulSoup("<footer>Here's the footer</footer>", "lxml")
# doc.find(text="INSERT FOOTER HERE").replace_with(footer)
# print(doc.name)




# soup = BeautifulSoup(html_doc, 'lxml')
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup.get_text())
# for link in soup.find_all('a'):
#     print(link.get('href'))