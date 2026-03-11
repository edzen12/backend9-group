# Задача: Система заказов в интернет-магазине
class Product: # продукт
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart: # корзина
    def __init__(self):
        self.items = [] # список товаров (Product)

    def add_product(self, product): # добавить товар в корзину    
        self.items.append(product)
        print(f"Добавлено {product.name}")

    def remove_product(self, name): # удалить товар по имени    
        for product in self.items:
            if product.name == name:
                self.items.remove(product)
                print(f"Удалено {name}")
                return 
        print("Товар не найден в корзине")

    def get_total(self): # посчитать общую сумму    
        total = 0
        for product in self.items:
            total += product.price
        return total

    def show_cart(self): # показать содержимое корзины
        print("Корзина товаров:")
        for product in self.items:
            print(f"{product.name} {product.price}")
        print(f"Итого: {self.get_total()} сом")


class Customer:
    def __init__(self,name, money):
        self.name = name
        self.money = money
   
    def pay(self, amount): # оплата
        if self.money >= amount:
            self.money -= amount
            print(f"{self.name} оплатил {amount} сом")
        else:
            print("Недостаточно средств")

p1 = Product('Ноутбук Acer Nitro', 35000)
p2 = Product('Мышка logitech', 1500)
p3 = Product('Клавиатура bloody', 3000)
cart = Cart()
customer = Customer("Гена Крокодил", 60000)
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.show_cart()
cart.remove_product('Мышка logitech')
cart.show_cart()
total = cart.get_total()
customer.pay(total)
print("Осталось денег: ", customer.money)
