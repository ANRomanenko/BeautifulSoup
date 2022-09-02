from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

work = Session()

work.get("https://my.skvot.io/", headers=headers)
response = work.get("https://my.skvot.io/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")

data = {"_csrf_token": token, "_username": "maxim.skachek@kyivstar.net", "_password": "qwerty123456"}

result = work.post("https://my.skvot.io/login_check", headers=headers, data=data, allow_redirects=True)

kyiv = work.get("https://my.skvot.io/ru/lesson/show/4070", headers=headers)
soup = BeautifulSoup(kyiv.text, "lxml")
dat = soup.find('div', class_='container')
name = dat.find('div', class_='box')
print(name)