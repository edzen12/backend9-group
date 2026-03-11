class Dish: #блюда
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Order: #Заказ
    def __init__(self):
        self.__items = [] #куда ложаться то что заказал клиент
    
    def add_dish(self, dish):
        self.__items.append(dish)
    
    def get_total(self):
        total = 0
        for dish in self.__items:
            total = total + dish.price
        return total
    
    def show_order(self):
        print("Вы заказали: ")
        for dish in self.__items:
            print(f" {dish.name} {dish.price}сом")
    
class Cafe:
    def __init__(self):
        self.menu = [
            Dish('Ташкентский плов', 320),
            Dish('Уйгурский лагман', 220),
            Dish('Манты', 330),
            Dish('Шашлык баранина', 220),
            Dish('Шашлык говядина', 210),
        ]
    
    def show_menu(self):
        print('Меню: ')
        for i, dish in enumerate(self.menu, start=1):
            print(f"{i} - {dish.name} {dish.price}")

    def get_dish_by_number(self, number):
        return self.menu[number - 1]


cafe = Cafe() # экземпляры
order = Order()
while True:
    cafe.show_menu()
    choice = input("Выберите номер блюда (нажмите 0 если хотите счет): ")
    if choice == "0":
        break
    
    dish = cafe.get_dish_by_number(int(choice))
    order.add_dish(dish)
    print(f"Добавлено: {dish.name}\n")

order.show_order()
print("Итого к оплате:", order.get_total(), "сом")