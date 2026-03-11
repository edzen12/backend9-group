import requests

res = requests.get('https://icanhazip.com/').text
with open('myIP.txt', 'w', encoding='utf-8') as file:
    file.write(res)
    print("Успешно записал в файл")