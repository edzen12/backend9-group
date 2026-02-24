user_ids = [101, 102, 103, 104] 
profiles = {
    101: {"name": "Aibek", "role": "admin"},
    102: {"name": "Nursultan", "role": "student"},
    103: {"name": "Adilet", "role": "teacher"}
}
while True:
    try:
        get_id = input("Введите свой ID: ")
        if get_id == 'stop':
            break
    except ValueError:
        print("Вводите только числа")
    try:
        print(profiles[int(get_id)])
    except KeyError:
        print("Профиль не найден")
    except NameError:
        print("Ошибка имени")
   


