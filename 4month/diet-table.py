import requests
import json 
import csv 
from bs4 import BeautifulSoup


def pusk():
    with open('all_categories.json', encoding='utf-8') as file:
        all_categories = json.load(file)

        for category_name, category_href in all_categories.items():

            report = [',', '-', ' ', "'"]
            for item in report:
                if item in category_name:
                    category_name = category_name.replace(item, '_')
            
            req = requests.get(category_href)
            src = req.text 

            # with open(f'diet-html/{category_name}.html', 'w', encoding='utf-8') as file:
            #     file.write(src)

            with open(f'diet-html/{category_name}.html', encoding='utf-8') as file:
                src = file.read()
            
            soup = BeautifulSoup(src, 'html.parser')

            alert_block = soup.find(class_='uk-alert-danger')
            if alert_block is not None:
                continue

            #собирали заголовки
            table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
            product = table_head[0].text
            calories = table_head[1].text
            proteins = table_head[2].text
            fats = table_head[3].text
            carbohyrates = table_head[4].text

            with open(f'csv/{category_name}.csv', 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (product,calories, proteins, fats, carbohyrates)
                )

            #собирали данные
            products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
            for item in products_data:
                products_tds = item.find_all('td')
                title = products_tds[0].find('a').text
                calories = products_tds[1].text
                proteins = products_tds[2].text
                fats = products_tds[3].text
                carbohyrates = products_tds[4].text

                with open(f'csv/{category_name}.csv', 'a', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (title,calories, proteins, fats, carbohyrates)
                    )

pusk()