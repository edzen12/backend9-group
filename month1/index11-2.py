# Исключения try except - обработка ошибок
# try - попытка,тот код который мы записываем и с ним все ок 
# except - исключая - встречает ту ошибку и дает возможность дейтсвия 
try:
    print(10/0)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except TypeError:
    print("Ошибка в несоответсвий типов данных(разные типы)")
except SyntaxError:
    print("Код неправильно написан, исправьте!")
except NameError:
    print("Ошибка в имени переменнных")