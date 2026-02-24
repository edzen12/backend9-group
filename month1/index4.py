name = 'Edzen Oichiev' 
age = 25
gender = 'Male'
biog = 'I\'m {1} backend developer, {0} {2}'.format(name, age, gender)
print(biog)

# индексы - это нумерация строк, индексы начинаются с нуля используя квадратные скобки []
# срезы [start:stop:step]
name = 'Gena Krocodil and Cheburashka'
print(name[5:13]+name[18:])
print(name[4:]) # начинаем от 4го до конца
print(name[:13]) # начинаем от нуля до 13 
print(name[::3]) # от начала и до конца, только с шагом 2

# f"" - f строка - когда мы можем переменные сразу давать имя переменных в фигурные скобки
bio2 = f"I'm {name} backend developer, \n{gender} and {age}"
print(bio2)


# input() - функция которая все принимает как тип данных str
fullname = input("Введите ваше имя: ")
age = int(input("Введите дату рождения (год): "))
print(f"Добро пожаловать {fullname}")
print(type(age))
print(f"Вам сейчас: {2025-age}")

# тупой калькулятор
num1 = int(input("введите первое число: "))
num2 = int(input("введите второе число: "))
print(f"Если + ответ: {num1+num2}")
print(f"Если - ответ: {num1-num2}")
print(f"Если * ответ: {num1*num2}")
print(f"Если / ответ: {num1/num2}")
print(f"Если ** ответ: {num1/num2}")
print(f"Если // ответ: {num1/num2}")
print(f"Если % ответ: {num1/num2}")