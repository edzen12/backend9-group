#1
# name = input("ВВедите свое имя: ")
# print(f"Привет, {name}!")

#2 
# age = int(input("ВВедите свой возраст: "))
# print(f"Вам через год будет {age+1}")

#3
# name = input("ВВедите свое имя: ")
# age = int(input("ВВедите свой возраст: "))
# gender = input("ВВедите свой gender: ")
# print(type(name))
# print(type(age))
# print(type(gender))

#4
# name = input("ВВедите свое имя: ")
# name = name.replace(' ', '') 
# print(f"{len(name)}")

# in - в
#5
# st1 = input("ВВедите любые предложения: ").lower() 
# if 'python' in st1:
#     print("Да, это про Python!")
# else:
#     print("Нет, не про Python.")

#6 
# fullname = input("ВВедите ФИО: ").title() 
# print(fullname)

#8
# st1 = input("ВВедите любые предложения: ").lower() 
# st1 = st1.replace(' ', '_')
# print(st1)

#9
# input() - ОН ВСЕГДА ПРИНМАЕТ str 
# chislo = int(input("ВВедите chislo: "))
# if chislo % 2 == 0:
#     print(f"четное число: {chislo}")
# elif chislo % 2 != 0:
#     print(f"Нечетное число: {chislo}")

#10
# chislo = int(input("ВВедите chislo: "))
# if chislo > 0:
#     print("Положительные")
# elif chislo < 0:
#     print("Отрицательная")
# else:
#     print("Ноль")

#11
# chislo = int(input("ВВедите chislo: "))
# if chislo == 5:
#     print("Отлично")
# elif chislo == 4:
#     print("Хорошо")
# elif chislo == 3:
#     print("«Удовлетворительно»")
# elif chislo == 2 or chislo == 1:
#     print("«Плохо»")
# else:
#     print("Пишите числа от 1го до 5ти включительно") 

#12
# chislo1 = int(input("ВВедите chislo 1: "))
# chislo2 = int(input("ВВедите chislo 2: "))
# if chislo1 > chislo2:
#     print(f"это {chislo1} больше")
# elif chislo1 < chislo2:
#     print(f"это {chislo2} больше")
# else:
#     print("Равны")

# №13
# password = input("Введите пароль: ")
# if password == "admin123":
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")

#14
# login = input("Введите login: ")
# password = input("Введите пароль: ")
# if len(password) <8:
#     print("Пароль должен быть больше 8 символов")
# elif password != password.title():
#     print("первая буква должна быть с большой")

#15
# dollar = float(input("Введите сколько у вас долларов: "))
# dollar_to_som = 87.30
# convert = dollar*dollar_to_som 
# print(convert)

#16
# slovo1 = input("Введите слово: ").lower()
# slovo2 = input("Введите слово: ").lower()
# slovo1 = slovo1.replace(" ", '')
# slovo2 = slovo2.replace(" ", '')
# if slovo1 == slovo2:
#     print("Совпадают")
# elif slovo1 != slovo2:
#     print("Разные") 

#17 калькулятор
# chislo1 = int(input("Введите первое число: "))
# simbol = input("Введите символ: ")
# chislo2 = int(input("Введите второе число: "))
# if simbol == '+':
#     print(chislo1+chislo2)
# elif simbol == '-':
#     print(chislo1-chislo2)
# elif simbol == '*':
#     print(chislo1*chislo2)
# elif simbol == '/':
#     print(chislo1/chislo2) 
# else:
#     print("Ошибка")

# 18
a = 10
b = 20
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print("равны")