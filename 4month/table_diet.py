import requests
from bs4 import BeautifulSoup
import json


url = 'https://health-diet.ru/table_calorie'

def get_html():
    req = requests.get(url).text 
    with open('table-diet.html', 'w', encoding='utf-8') as file:
        file.write(req)

# get_html()

def get_category_link():
    with open('table-diet.html', encoding='utf-8') as file:
        src = file.read()
    
    soup = BeautifulSoup(src, 'html.parser')
    all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
    all_categories_dict = {} 
    for item in all_products_hrefs:
        item_text = item.text 
        item_href = 'https://health-diet.ru'+item.get('href')
        all_categories_dict[item_text] = item_href
    with open('all_categories.json', 'w', encoding='utf-8') as file:
        json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)   
    
# get_category_link()