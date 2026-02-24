users = ("admin", "manager", "student", "guest") 
permissions = {
    "admin": "полный доступ",
    "manager": "доступ к управлению",
    "student": "доступ к обучающим материалам"
}
while True:
    login = input("введите логин: ")
    if login == 'exit':
        break
    if login in users:
        try:
            print(permissions[login])
        except KeyError:
            print("Доступ не назначен")
    elif login not in users:
        print("Нет такого логина, введите заново")
         