car_km_to_h = 100
if car_km_to_h >= 100:
    print("Ferrary")
else:
    print("Tico")
######### Тернарный оператор (когда код пишется в одну строку)
car_km = 50 
print('Ferrary' if car_km >= 100 else 'Tico')
# №№№№№№№№№
age = 19
message = "Добро пожаловать" if age > 18 else "Запрещен вход"
print(message)
# №№№№№№№№№№№
my_passwords = ["qwerty", "12345678"]
user_input = "qwerty"
access = "разрешен" if user_input in my_passwords else "запрещен"
print("Вход " +  access)

# № задача №1
# есть a = 2, b = 5, если а больше b (выведите "А крутой"), если b больше (выведите "B Имбовый"), присвойте это новой переменной max
a,b = 1, 5 # множественное присвоение
max = "А крутой" if a > b else "B Имбовый"
print(max)

# № задача №2 тоже самое что выше, только еще одна переменная добавилась, выведите все в одну строку, присвойте это новой переменной max
a, b, c = 15, 93, 22 # множественное присвоение
max2 = "А крутой" if a > b and a > c else "B Имбовый" if b>c else 'C дерзкий' 
print(max2)