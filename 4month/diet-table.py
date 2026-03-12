import requests
import json 
import csv 


with open('all_categories.json', encoding='utf-8') as file:
    all_categories = json.load(file)
    

    for category_name, category_href in all_categories.items():

        report = [',', '-', ' ', "'"]
        for item in report:
            if item in category_name:
                category_name = category_name.replace(item, '_')
        
        req = requests.get(category_href)
        src = req.text 

        with open(f'diet-html/{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)