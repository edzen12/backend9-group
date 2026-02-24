# int - целые числа
# float - числа с остатком
# bool - True-1 False-0
# str - строка '' "" """""" ''''''
# list - списки [3,4,56.56, "привет"]
    # вложенные списки - names = ['Gena', 'Pasha', ["Nastya", [18, 19], 'Artem']]
# tuple - кортеж () такой же как list, но он НЕизменяемый
# set - множества {1,2,3,1,2,3} изменяемый, неиндексируемый, содержащий только уникальные значения
# dict - dictionary - словарь {key:value} изменяемый, неиндексируемый

# цикл: 
#     for-для 

age = [10,11,12,13,14,15]  
name = ['gena', 'artem', 'niko']
names = []
for i in name:
    names.append(i.title())
print(names)
#######
contact_names = {
    'genadiy': '0507888994',
    'artemiy': '0507888995',
    'nikolai': '0507888996',
}
phonesDict = []
for i in contact_names.values():
    phonesDict.append(i)
print(phonesDict)

####
playlist = ['Молмолум', "Кечки Бишкек", "Кыргызстан"]
for muz in playlist:
    print("сейчас играет:",muz)
# №№№№№
all_fruits = ['Banan',  'Apple', 'Orange','Ananas', 'Cherry', 'Greip']
my_favorites = ['Banan', 'Ananas']
for item in all_fruits:
    if item in my_favorites:
        print("Мое любимое:", item)
    else:
        print("Фуу, не люблю такое:", item)
# №№№№№№
# ребята, сделайте список из 20 чисел, только так чтобы все 20 чисел были четные
# range(start:stop:step)
chetnye = []
for i in range(0, 40, 2):
    chetnye.append(i)
print(chetnye)
#######
chetnye = []
for i in range(40):
    if i % 2 == 0:
        chetnye.append(i)
print(chetnye)
####### 2
# Дан список целых чисел
# Перебирать числа, a kак только встретится число 139, прекратить обработку списка.
# Все чётные числа пропускать.
# Вывести на экран только нечётные числа, которые идут до числа 139.
chisla = [5,6,123,55,44,34,139, 45,342]
for num in chisla:
    if num == 139:
        break
    if num % 2 == 0:
        continue
    print(num)
