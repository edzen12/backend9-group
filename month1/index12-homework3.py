#Дан список целых чисел:
numbers = [5, 10, 15, 20, 25] 
while True:
    ElementIndex = input('Введите индекс элемента списка: ')
    if ElementIndex == 'exit':
        break
    try:
        print(numbers[int(ElementIndex)])
    except IndexError:
        print("Ошибка, неправильный индекс")
    except ValueError:
        print("пользователь ввёл не число")
    
   
