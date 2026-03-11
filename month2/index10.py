def hello():
    print('Hello guys!')

gena = hello # функцию присвоили переменной и эта переменная стала функцией
print(type(gena))
######
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    message = func('Hello Python!')
    print(message)

speak(shout)
######
def inc(x):
    return x+1

def dec(x):
    return x-1

def operate(func, x):
    res = func(x)
    return res 

print(operate(inc, 4))
######

def outer():
    def inner():
        print("Внутренняя функция")
    return inner

outer()()
# 
new_func = outer()
new_func()
# Декоратор - функция, которая принимает другую функцию в качестве аргумента, расширяет или модифицирует её поведение, и возвращает её, не меняя исходный код
# Функция outer  возвращает другую функция, это и есть идея декоратор

def before_arter(func):
    def wrapper():
        print("Перед вызовом функции")
        func()
        print("После вызовом функции")
    return wrapper

@before_arter # декоратор
def say_hi():
    print("Привет друг")

say_hi()
# №№№№№№№№


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(a,b):
    return a+b 

add(3,4)
########
@logger
def delete_user(username):
    print(f"Пользователь {username} удалён")
    return True

delete_user("Gena")
#########
@logger
def transfer(balance, amount):
    if amount > balance:
        return "Недостаточно средств"
    return balance - amount

transfer(1000, 250)
########## 

# @property декоратор
#     getter 
#     setter 
#     deleter
# Декоратор @property в Python — это встроенный инструмент, который превращает метод класса в «свойство» (атрибут), позволяя обращаться к нему без круглых скобок (obj.name вместо obj.name()), сохраняя при этом логику методов (геттеров/сеттеров). Он реализует инкапсуляцию, обеспечивая безопасное чтение, изменение и валидацию данных, делая код более читаемым и гибким. 
class Person:
    def __init__(self, name ):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        return self.__name
    
    @name.deleter
    def name(self):
        print("Удаляем имя")
        del self.__name

    def info(self):
        print(self.__name, 'черт')


per1 = Person('Gena')
print(per1.name) # getter
per1.name = 'Giras' # setter
per1.info()
del per1.name # deleter
per1.info()


