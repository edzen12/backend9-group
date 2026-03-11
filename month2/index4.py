# ООП пайтон
# Принципы ООП:
#     Наследование - создание новых классов на основе существующих
#     Инкапсуляция - это сокрытие данных
        # public - открытый
        # _protected - защищенный
        # __private - приватный
#     Полиморфизм - один интерфейс, много реализаций
#     Абстракцию - выделение существенных признаков
class Animal:
    def __init__(self, name, age, color,classification, life=100, damage=0):
        self.name = name
        self.__age = age # атрибут класса
        self.color = color
        self.classification = classification
        self.life = life
        self.damage = damage
    
    def set_damage(self):
        return self.damage
    
    def get_damage(self, value):
        if self.life>0:
            self.life -= value
        elif self.life <= 0:
            print(self.name, 'умер')
    
    def reNameColor(self, newName, newColor):
        self.name = newName
        self.color = newColor

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >=1 and new_age<20:
            self.__age = new_age
            return self.__age
        else:
            print("недопустимое значение")

    def info(self):
        return f"Имя: {self.name} возраст: {self.__age} {self.color} {self.classification}"

class Cat(Animal):
    def mau(self):
        return "Мяу-мяу"
    
    def get_damage(self, value):
        super().get_damage(value)
        print(f"ах ты собака! Жизнь у кошки:{self.life}%")
    
class Dog(Animal): 
    def gav(self):
        return 'gav-gav'  
    
    def get_damage(self, value):
        super().get_damage(value)
        print(f"чертова шаверма! Жизнь у собаки:{self.life}%")

cat1 = Cat('felix', 2, 'черная', 'Домашние животные', damage=15)
dog1 = Dog('gar', 3, "белая", 'Домашние животные', damage=25)

dog_damage = dog1.set_damage()
cat_damage = cat1.set_damage()
cat1.get_damage(dog_damage)
dog1.get_damage(cat_damage)
dog1.get_damage(cat_damage) 
cat1.get_damage(dog_damage)
cat1.get_damage(dog_damage)
dog1.get_damage(cat_damage)
print(cat1.info())
cat1.reNameColor("Мадонна", 'Белая')
print(cat1.info())
# 1) Сделать так чтобы когда чья та жизнь падает на ноль, выходило сообщение что он умер и прекратить получение урона
# 2) Сделать метод для изменения цвета и метод для изменения имени
# 3) Добавить новый атрибут classification(классификация) животных