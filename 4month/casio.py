import requests
from bs4 import BeautifulSoup
import csv


url = 'https://shopcasio.bstarco.kg/collections/g-shock'
headers = {
    'User-Agent': 'Mozilla/5.0'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('a', href=lambda x: x and 'products/' in x)
data = []
for product in products:
    title = product.find('h3')
    price_block = product.find('div', class_='flex font-bold')
    if title:
        name = title.text.strip()
    else:
        continue
    if price_block:
        price = price_block.find('div').text.strip()
    else:
        price = None 
    link = 'https://shopcasio.bstarco.kg/'+product['href']
    data.append({
        'Название':name,
        'Цена':price,
        'Фото':link,
    })
    
with open('gshock.csv', 'w', encoding='utf-8') as file:
    fieldnames = ['Название', 'Цена', 'Фото']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)