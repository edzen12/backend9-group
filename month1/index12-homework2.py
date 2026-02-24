products = {
    "apple": 100,
    "banana": 80,
    "orange": 120
}
while True:
    product = input("Введите товар: ")
    if product in products:
        print(f'Цена: {products[product]}')
    if product == 'stop':
        print("Спасибо что пользовались нашим приложением")
        break
    if product not in products:
        print('Такого товара нет')
        
    