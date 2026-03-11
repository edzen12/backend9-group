class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.books = []
        self.knowledge = 0 #знания
        self.is_ready_to_work = False #готовность к работе
        self.prog_languages = {}
    
    def add_points(self, points):
        self.knowledge += points
        if self.knowledge > 1000:
            print("Студент готов к работе")
            self.is_ready_to_work = True
    
    def read_book(self, book):
        self.books.append(book)
        self.add_points(100)

    def do_homework(self):
        self.add_points(20)
    
    def do_project(self):
        self.add_points(50)
    
    def learn_languages(self, lang, points):
        if points<1 or points>100:
            raise ValueError
        else:
            self.prog_languages[lang] = points
            self.add_points(points)
    
    def info(self):
        return f"имя: {self.name} {self.lastname}\nя читал {self.books}\nМои знания{self.knowledge} готовность к работе: {'готов' if self.is_ready_to_work else 'не готов'}\nЯ знаю {self.prog_languages}"

kuma = Student('Kuma', 'Backend')
print(kuma.info())
kuma.read_book('Основы python')
kuma.do_homework()
kuma.do_project()
kuma.do_project()
kuma.do_project()
kuma.read_book("Грокаем алгоритмы")
kuma.read_book("Чистая архитектура")
kuma.learn_languages('python',99)
kuma.learn_languages('SQL',98)
kuma.learn_languages('DjangoRest',99)
kuma.learn_languages('HTML',90)
kuma.learn_languages('CSS',90)
kuma.learn_languages('Django',99)
print(kuma.info())
