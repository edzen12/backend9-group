# Операторы
#     Арифметические + - * / ** // %
#     Сравнения > < >= <= != ==
#     Логические операторы and-и, or-или, not-не

# Типы данных
#     int 123, -453 Неизменяемый
#     float 45.567, -345235.4 Неизменяемый
#     bool True=1 False=0 Неизменяемый
#     str - строка 'str1', "str2", '''tr3''', """tr3""" Неизменяемый
#     list - список [] изменяемый
#     tuple - кортеж () Неизменяемый
#     set - множества {1,2,1,2,3}  изменяемый
#     dict - словарь {key:value} изменяемый
#     None - пустой

# Исключения / обработка ошибок
#     try код который должен работать, except  

# Условия 
#     if elif else 

# Циклы 
#     for - для
#     while - пока, он с условием

# Функции 
#     Встроенные функции 
#         print(), len(), input(), type()
#     Пользовательские функции (То что мы сами пишем)
#         lambda - анонимные функции
#         def - обычные функции
        
def GetNameAge(name):
    print(name,'Салам')

GetNameAge('Gena')
###########
def multiFruit(name1, name2):
    return f"У нас получился сок из {name1} и {name2}"

print(multiFruit('Ананас', "Клубника"))
#########
# pass - заглушка, чтобы код не вызывал ошибку


def distinct(seq): 
    n = set()
    result = []
    for i in seq:
        if i not in n:
            n.add(i)
            result.append(i)
    return result

print(distinct([1, 1, 2,3,3,3,2,3,5]) )
###########
def no_boring_zeros(n):
    return int(str(n).rstrip('0'))

print(no_boring_zeros(1450)) # должны получить: 145
print(no_boring_zeros(960000)) # должны получить: 96
#########
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    pass


spisok = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
print(goose_filter(spisok))