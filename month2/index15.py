# Наследование
#     наследование 
#     множественное наследование
# Инкапсуляция
#     public - публичные
#     _protected - защищенные
#     __private - приватные
# Полиморфизм - принцип ООП, позволяющий использовать один интерфейс (имя метода или функции) для различных типов объектов, обеспечивая гибкость кода

class Dog:
    def speak(self):
        return 'gav-gav'

class Cat:
    def speak(self):
        return 'мяу-мяу'

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())
#######################

# Полиморфизм через наследование
class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CardPayment(Payment):
    def pay(self, amount):
        return f"Оплата картой: {amount}"

class CryptoPayment(Payment):
    def pay(self, amount):
        return f"Оплата криптой: {amount}" 

def process(payment:Payment):
    print(payment.pay(1000))

process(CardPayment())
process(CryptoPayment()) 
# Python не проверяет класс, наследование или интерфейс.
# Он проверяет только одно:
# Есть ли у объекта нужный метод / атрибут в момент вызова

# №№№№№№№№№№№№№
# Ключевая идея Полиморфизма в python основана на duck typing 
# Утиная типизация (duck typing) в Python — это принцип, при котором тип объекта определяется его поведением (методами и свойствами), а не явным указанием класса. 
# Суть: «Если это выглядит, плавает и крякает как утка, то это утка». В Python не проверяют, является ли объект унаследованным от конкретного класса, а сразу используют его методы. 
class FileLogger:
    def write(self, message):
        print("Файл:", message)

class SocketLogger:
    def write(self, message):
        print("Сокет:", message)

def log(writer):
    writer.write('Успех')

log(FileLogger()) # log не знает что за объект ей передали
# не проверяет тип
# не проверяет класс
# просто вызывает метод write()
log(SocketLogger())

# №№№№№№№№№№№№№№№№№№№ Задача
# Есть функция notify(sender).
# Она должна вызывать метод send(message) у переданного объекта.
# Нужно:
# 1) Создать два разных класса без общего родителя:
#     EmailSender
#     SmsSender
# 2) В каждом классе реализовать метод send(self, message)
# 3) Вызвать notify() для каждого объекта
class EmailSender:
    def send(self, message):
        print('E-mail', message)

class SmsSender:
    def send(self, message):
        print("SMS", message)

def notify(sender):
    sender.send("Привет!")

notify(EmailSender())
notify(SmsSender())


# №№№№№№№№№№№№№
# Есть функция export(data, exporter).
# Она:
# 1)получает данные (data)
# 2)передаёт их объекту exporter
# 3)вызывает у него метод export(data)
# Нужно:
# 1)Создать два класса-экспортёра без наследования:
#     CsvExporter
#     XmlExporter
# 2)В каждом реализовать export(self, data)
# 3)Вызвать export() с разными экспортёрами
class CsvExporter:
    def export(self, data):
        print("CSV экспорт", data)

class XmlExporter:
    def export(self, data):
        print("XML экспорт", data)

def export(data, exporter):
    exporter.export(data)

data = {"name": "Alex", "age": 25}

export(data, CsvExporter())
export(data, XmlExporter())



# Задача №3
# Условие: Есть функция handle(data, handler).
# Она должна вызывать у переданного объекта метод handle(data) и выводить результат.
# Нужно:
# 1)Создать два обработчика без наследования:
#     UpperHandler — переводит строку в верхний регистр
#     TrimHandler — убирает пробелы по краям
# 2)Каждый обработчик должен реализовать handle(self, data)
# 3)Последовательно применить обработчики к данным

def handle(data, handler):
    return handler.handle(data)

text = "   hello world   "