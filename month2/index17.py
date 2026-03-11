class Human:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    
    def info(self):
        print(f"{self.last_name} {self.first_name} {self.age}", end=' ')

class Student(Human):
    def __init__(self, last_name, first_name, age, spec, group, rating):
        super().__init__(last_name, first_name, age)
        self.spec = spec
        self.group = group
        self.rating = rating
    
    def info(self):
        super().info()
        print(f"Проф: {self.spec}, Группа: {self.group}, Рейтинг: {self.rating}")

class Teacher(Human):
    def __init__(self, last_name, first_name, age, spec, exp):
        super().__init__(last_name, first_name, age)
        self.spec = spec
        self.exp = exp
    
    def info(self):
        super().info()
        print(f"Предмет: {self.spec}, Опыт: {self.exp} лет")
    
class Graduate(Student): # Выпускник
    def __init__(self, last_name, first_name, age, spec, group, rating, topic):
        super().__init__(last_name, first_name, age, spec, group, rating)
        self.topic = topic
        
    def info(self):
        super().info()
        print(f'Речь: {self.topic}', end=' ')

group = [
    Student("Grande", 'Arianna', 18, 'ФМИТ', 'ПОВТАС', 5),
    Graduate('Мамет', "Назаров", 22, 'ФМИТ', 'ИТАС', 4, "Создание сайта на Django"),
    Teacher('Башкирова', "Аля", 45, 'Фронтенд разработка', 20)
]
for i in group:
    i.info()