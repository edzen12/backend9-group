num = [6,7,8]
beg = [1,56,32,2,3,4,5,6,[45,56,67,67], 6,6,6,6]
# когда внутри одного списка, есть еще список, он называеся - вложенным списком 
beg.extend(num)
beg.append({9, 10})
beg.insert(0, 0)
beg.remove(5)
print('вы удалили',beg.pop(3))
beg.reverse() 
print(beg) 


# Типы данных
# int - целые числа
# float - числа с остатком
# bool - True-1 False-0
# str - строка "" '' """""" ''''''
# list - списки [] изменяемый тип данных, индексируемый
# tuple - кортеж () неизменяемый тип данных, индексируемый
# set - множетва {} изменяемый, он всегда хранит только уникальные значения, неупорядоченный, неиндексируемый
animals = {'crocodil', 'begemot', 'jiraf', 'begemot', 'jiraf',1,2,3,1,2,3}
print(animals)
#####

# dict - dictionary - словарь {key:value} - изменяемый тип данных, неиндексируемый

# У нас будет программа, которая будет давать нам выбрать
# если мы выберим 1-добавлять новое имя и номер
# если мы выберим 2-изменить существующее имя и номер
# если мы выберим 3-удаляет существующее имя и номер
contact_phone = {
    'Adilet':'0707707707', 
    'Gena':'0505505505',
}
number = input("1-добавлять\n2-изменить\n3-удалить\nВыберите действие:")
if number == '1':
    name = input("Имя: ").title().strip()
    phone = input("номер: ")
    contact_phone[name] = phone
    print("Успешно добавлено")
    print(contact_phone)
elif number == '2':
    old_name = input("старое имя: ").title().strip()
    new_name = input("новое имя: ").title().strip()
    new_phone = input("новый телефон: ")
    del contact_phone[old_name]
    contact_phone[new_name] = new_phone
    print("Успешно изменено")
    print(contact_phone)
elif number == '3':
    name = input("Имя: ").title().strip()
    del contact_phone[name]
    print("Успешно удалено")
    print(contact_phone)

