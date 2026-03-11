class Task:
    def __init__(self, title, is_done=False): # магический метод
        self.title = title 
        self.is_done = is_done
    
    def complete(self): # выполнена задача
        self.is_done = True
    
    def to_string(self):
        return f"{self.title}|{int(self.is_done)}"

    @staticmethod # способ объявить метод который относится к классу, но не к конкретному объекту
    def from_string(line):
        title, is_done = line.strip().split('|')
        return Task(title, bool(int(is_done)))
    

class TodoList:
    def __init__(self, filename='tasks.txt'):
        self.__tasks = [] # приватный атрибут
        self.filename=filename
        self.load() # метод который мы создадим в будущем
    
    def add_task(self, task):
        self.__tasks.append(task)
        self.save()

    def delete_task(self, number):
        if 1 <= number <= len(self.__tasks):
            del self.__tasks[number-1]
            self.save()
            print("Задача удалена")
        else:
            print("Неверный номер задачи")
    
    def show_tasks(self):
        print("Список задач:")
        for i, task in enumerate(self.__tasks, start=1):
            status = '✓' if task.is_done else "ⓧ"
            print(f"{i}. {task.title} {status}")
    
    def complete_task(self, number):
        if 1 <= number <= len(self.__tasks):
            self.__tasks[number-1].complete()
            self.save()
            print("Задача выполнена")
        else:
            print("Неверный номер задачи")
    
    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for task in self.__tasks:
                file.write(task.to_string() + '\n')

    def load(self):
        self.__tasks = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    self.__tasks.append(Task.from_string(line))
        except FileNotFoundError:
            pass

todo = TodoList()
while True:
    print('1-Добавить задачу')
    print('2-Показать задачу')
    print('3-Выполнить задачу')
    print('4-Удалить задачу')
    print('0-Выход') 
    choice = input("Выбор: ")
    if choice == '1':
        title = input("Введите задачу: ")
        todo.add_task(Task(title))
    elif choice == '2':
        todo.show_tasks()
    elif choice == '3':
        number = int(input("Номер задачи: "))
        todo.complete_task(number)
    elif choice == '4':
        number = int(input("Номер задачи: "))
        todo.delete_task(number)
    elif choice == '0':
        break


# CRUD 
#     Create
#     Read
#     Update
#     Delete