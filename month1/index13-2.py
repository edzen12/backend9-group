allowed_users = ["admin", "teacher", "student", "guest"] 
login_attempts = {} 
blocked_users = set() 
logged_users = set()
while True:
    login = input("Введите логин: ").strip() 
    if login == "exit":
        break 
    try:
        if login in blocked_users:
            raise PermissionError("Пользователь заблокирован")
        if login not in allowed_users:
            login_attempts[login] = login_attempts.get(login, 0) + 1
            if login_attempts[login] >= 3:
                blocked_users.add(login)
            raise ValueError("Недопустимый логин")
        logged_users.add(login)
        print("Вход разрешён") 
    except ValueError as e:
        print(e) 
    except PermissionError as e:
        print(e) 
    finally:
        print("Попытки:", login_attempts)
        print("Заблокированные:", blocked_users)
        print("В системе:", logged_users)
