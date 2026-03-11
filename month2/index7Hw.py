# Задача №1: Мини-банк 
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance 
 
    def deposit(self, amount): #пополнить счёт
        self.balance += amount
        print(f"Успешно пополнили баланс на {amount}сом")
        return self.balance
    
    def withdraw(self, amount): #снять деньги
        if amount <= self.balance:
            self.balance -= amount
            print(f"Успешно сняли {amount}сом\nОсталось: {self.balance}сом")
        else:
            print("Недостаточно средств")

    def info(self): #показать баланс
        print(f"Владелец: {self.owner} {self.balance}сом")

gena = Account('Gena Crocodil') 
gena.deposit(1000)
gena.info() 
gena.withdraw(50)
# №№№№№№№№№№№№№№№№№№
# Задача 2: Система библиотеки
class Book:
    def __init__(self, title, author):
        self.title = title  
        self.author = author  
        self.is_available = True #доступна ли книга 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book): #добавить книгу в библиотеку
        self.books.append(book)

    def show_books(self): #показать все книги и статус
        print("Список книг: ")
        for book in self.books:
            status = 'Доступна' if book.is_available else 'Недоступно'
            print(f"{book.title}:{status}")

    def borrow_book(self,title): # взять книгу
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print("Книга выдана")
                else:
                    print("Книга недоступна")
        print("Книга не найдена")

    def return_book(self,title): # вернуть книгу
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print("Книга возвращена")
                else:
                    print("Эта книга и так была в библиотеке")
                return    
        print("Книга не найдена")

biblioteka = Library()
biblioteka.add_book(Book("Python за 100 дней", "Gena Алкашов"))
biblioteka.add_book(Book("ООП принципы", "Галкин Матвей Абрамович"))
biblioteka.add_book(Book("Чистый код", "Мартин Ли"))
biblioteka.show_books()
biblioteka.borrow_book("Python за 100 дней")
biblioteka.borrow_book("Python за 100 дней")
biblioteka.return_book("Python за 100 дней")
biblioteka.borrow_book("Чистый код")
biblioteka.show_books()