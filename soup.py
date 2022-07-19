import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# url = 'https://allo.ua/ru/products/mobile/klass-kommunikator_smartfon/'
#
# response = requests.get(url)

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'lxml')
print(rel_soup.a['rel'])

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)

# soup = BeautifulSoup(html_doc, 'lxml')
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup.get_text())
# for link in soup.find_all('a'):
#     print(link.get('href'))