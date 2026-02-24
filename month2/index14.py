# Задача: Магазин
# Есть: товар, скидка, VIP-товар (имеет и цену, и скидку)

# Класс Product
#     имеет приватный атрибут __price
#     в __init__(price) цена должна быть > 0
#     метод get_price() возвращает цену

# Класс Discount
#     имеет приватный атрибут __discount
#     в __init__(discount) скидка от 0 до 50
#     метод get_discount() возвращает скидку

# Класс VIPProduct(Product, Discount)
#     принимает price и discount
#     умеет считать финальную цену
#     Метод:
#     get_final_price()
#     Формула: price - price * discount / 100