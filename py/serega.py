from bs4 import BeautifulSoup
import requests

url = input("Paste your link ")
page = requests.get(url)
print(page.status_code)
filteredNews = []
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
allNews = soup.findAll('a', class_='btn_green_white_innerfade btn_medium market_commodity_buy_button')
for data in allNews:
    if data.find('span', class_='market_commodity_orders_header_promote') is not None:
        filteredNews.append(data.text)
for data in filteredNews:
    print(data, end="")