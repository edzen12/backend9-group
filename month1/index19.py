notebook = ['acer', 'lenovo', 'macbook', 'huawey bey'] 
#1
nb = []
for note in notebook:
    nb.append(note.title()) 
print(nb) 
#############
# map(function, list) - применяет заданную функцию к каждому элементу одного или нескольких итерируемых объектов:
# Списки (list), Кортежи (tuple), Строки (str), Множества (set), 
# Словари (dict), Диапазоны (range)
print(list(map(str.upper, notebook)))
# 2
# Вам надо подсчитать сколько букв в каждом слове и показать это в терминале
res_number = []
for i in notebook: 
    res_number.append(len(i))
print(res_number)
########
print(list(map(len, notebook)))
#########
#3 есть список с дробными числами, все с пятью десятичными знаками. И вот вам надо округлять каждый элемент, но с каждый моментом на один знак больше чем предыдущий
chaos_number = [3.56789, 5.36431, 4.46433, 6.54466, 7.46746]
print(list(map(round, chaos_number, range(1,6))))
#######
print(list(map(lambda x: x*2, notebook)))
#######
scores = [70,65,78, 89,100, 67,98]
print(list(filter(lambda x: x>80, scores)))
########
polindrom = ['anna', 'madam', 'gena', 'woman', 'ded', 'zakaz']
res = list(filter(lambda word: word==word[::-1], polindrom))
print(res)
#######
scores2 = [70,65,78, 89,10, 67,98, 467]
numbers_pos = list(filter(lambda n: n%2==0, scores2))
print(numbers_pos)
#######
from functools import reduce
maxnum = reduce(lambda a,b: a if (a>b) else b, scores2)
print(maxnum)
#######

# Задача 1. Нужно: Оставить слова длиной больше 4, Привести их к верхнему регистру, Получить список
words = ["django", "flask", "fastapi", "api", "rest", "graphql", "sql"]

# Задача 2. Нужно получить список имён пользователей возраст больше или равным 18
users = [
    {"name": "Ivan", "age": 17},
    {"name": "Anna", "age": 22},
    {"name": "Oleg", "age": 19},
    {"name": "Kate", "age": 16},
]
# Задача 3. Нужно оставить числа, которые делятся на 2 и НЕ делятся на 3
nums = [1, 2, 3, 4, 6, 8, 9, 12, 15, 16, 18]
