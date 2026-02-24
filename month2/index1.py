# ООП - объектно-ориентированное программирование
# self в Python — это обязательный первый параметр методов экземпляра класса, позволяя обращаться к его атрибутам и другим методам
# Методы класса фактически представляют функции, которые определенны внутри класса и которые определяют его поведение
class Cat:
    def __init__(self, name, age): # магическим метод - конструктор класса
        self.name = name  # атрибут класса
        self.age = age 
    
    def sound(self): # метод класса / функцию
        return "мяу-мяу"
    
    def rename(self, newName):
        self.name = newName
        return self.name
    
    def info(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nЗвук: {self.sound()}"

cat1 = Cat('Felix', 2) # экземпляр 
cat2 = Cat('Барсик', 5) # экземпляр 
print(cat1.info())
print(cat2.info())
cat2.rename('Fedya')
print(cat2.info())