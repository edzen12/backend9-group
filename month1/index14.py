# Функции:
#     Встроенные функции:
#         print()
#         len()
#         type()
#         int()
#     Пользовательские функции:
#         lambda - анонимные функции
#         def функция которую мы сами создаем

# функция - это блок кода, который выполняет определенную задачу

def get_name(name): # функция с аргументом (то что в скобках)
    print('Добро пожаловать: ', name)

get_name("Арген")
get_name("Гена")
get_name("Мирлан")
get_name("Бека")
get_name("Умар")
###########
def sumTwoNumber(a, b):
    return a+b
print(sumTwoNumber(5,6))

# №№№№№№№№

def calcaulator():
    num1 = int(input("Введите первое число: "))
    simbol = input("Введите + - * / ")
    num2 = int(input("Введите второе число: "))
    if simbol == '+':
        return num1+num2
    elif simbol == '-':
        return num1-num2
    elif simbol == '*':
        return num1*num2
    elif simbol == '/':
        return num1/num2
    else:
        print("Ошибка")

print(calcaulator())